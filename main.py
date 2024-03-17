import requests
import validators
import os, shutil
import time
import zipfile
import concurrent.futures

trip_aws_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip"
]


def fetchFile(url, file_path):
    if validators.url(url):
        r = requests.get(url)
        if r.status_code == 200:
            with open(file_path, 'wb') as w:
                w.write(r.content)
            return True
        else:
            return False
    else:
        False


def getFilePath(url, path_downloads):
    file_name = url.split('/')[-1] 
    file_path = os.path.join(path_downloads, file_name)
    return file_path


def downloadFile(URLs, path_downloads, workers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_url = {executor.submit(fetchFile, url, getFilePath(url,path_downloads)): (url, getFilePath(url,path_downloads)) for url in URLs}
        for future in concurrent.futures.as_completed(future_to_url):
            url, file_path = future_to_url[future]
            print("Downloading file from: ", url)
            try:
                result = future.result()
                if result:
                    print("File downloaded successfully and saved to:", path_downloads)
                    extractFile(file_path, path_downloads)
                else:
                    print("FAILED to download file from: ", url)
            except Exception as exc:
                print(f"FAILED to download file from {url}: {exc}")

    
def extractFile(file_path, pathToExtract):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(pathToExtract)      
    os.remove(file_path)
    shutil.rmtree(pathToExtract+'\__MACOSX')
    print("FILE IS READY")


def main():
    path_downloads = 'fast_downloads'
    workers = 8

    if not os.path.exists(path_downloads):
        os.mkdir(path_downloads)
    
    downloadFile(trip_aws_uris, path_downloads, workers)
      

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- {} seconds ---".format(time.time() - start_time))
