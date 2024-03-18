## File Download Optimization
This README outlines the optimization process for downloading multiple large-sized Python files from URIs using HTTP.

### Introduction
In this project, I aimed to download multiple Python files ranging from 49 MB to 220 MB in size from URIs using HTTP. Initially, the files were in zip format, which were then extracted to CSV files. Subsequently, the zip files were deleted to conserve storage space.

### Optimization Process
#### Initial Approach
My initial implementation utilized the `Requests` library in Python to download the files sequentially. While functional, this approach had limitations in terms of performance and efficiency.
#### Optimization with ThreadPoolExecutor
To improve performance and reduce download times, I optimized the code by leveraging the `ThreadPoolExecutor` from the `concurrent.futures` module. This allowed parallelization of file downloads, significantly reducing the overall duration.
By utilizing ThreadPoolExecutor, I achieved a remarkable improvement in download times. The duration of file downloads was reduced by approximately `50%` compared to the initial sequential approach.

### Performance Results
#### Initial Approach:
Total Duration: `497 seconds`
#### Optimized Approach (ThreadPoolExecutor):
Total Duration: `236 seconds`

### Conclusion
Through optimization with ThreadPoolExecutor, I successfully reduced the duration of file downloads by `half`, significantly improving the efficiency of the process. This optimization not only enhances performance but also demonstrates the effectiveness of leveraging concurrency for parallel processing tasks.
