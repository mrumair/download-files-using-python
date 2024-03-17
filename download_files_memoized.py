import requests
import validators
import os, shutil
import time
import zipfile
import aiohttp
import asyncio

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

# # for memory-limit...
# def downloadFile(url, file_path):
#     print("FETCHING FILE")
#     if validators.url(url):
#         with requests.get(url, stream=True) as r:
#             r.raise_for_status()
#             with open(file_path, 'wb') as f:
#                 for chunk in r.iter_content(chunk_size=8192):
#                     f.write(chunk)
#         return file_path
#     else:
#         print ("Invalid URL ", url)


async def downloadFile(url, file_path):
    print("FETCHING FILE...")
    if validators.url(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                content_to_write = await r.read()
                with open(file_path, 'wb') as w: 
                    w.write(content_to_write)
    else:
        print ("Invalid URL ", url)

    

def extractFile(file_path, pathToExtract):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(pathToExtract)      
    os.remove(file_path)
    shutil.rmtree(pathToExtract+'\__MACOSX')
    print("FILE IS READY")


def main():
    path_downloads = 'testing'
    if not os.path.exists(path_downloads):
        os.mkdir(path_downloads)

    url = download_uris[0]
    file_name = url.split('/')[-1] 
    file_path = os.path.join(path_downloads, file_name)
    
    asyncio.run(downloadFile(url, file_path))
    extractFile(file_path, path_downloads)
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- {} seconds ---".format(time.time() - start_time))
