# Sacumen Test Solution


## Introduction:
This repository provides solution to below problem:
>There are couple of files in a directory like images (jpg, png, svg, and webp), media (mp3, mp4, mpeg4, wmv, 3gp, and webm), and documents (doc, docx, csv, and pdf).
The module should read all the files from the directory and its subdirectory, upload all the images and media files to AWS S3, and all the documents to Google cloud storage.
write a generic module which can be utilized as per need. The types of files to transfer to S3 and google cloud storage should be configurable.

## Description
This repository allows you to upload files from directory and it's subdirectory in AWS S3 and Google cloud storage. This upload will happen based on file types which configured in `settings.py`

## How to Install and Run the Project
1. Create AWS S3 storage bucket and set list, read, write persmission for python script. For more information follow upto step #5 [in article](https://towardsdatascience.com/how-to-upload-and-download-files-from-aws-s3-using-python-2022-4c9b787b15f2).
2. Set environment variables `AWS_BUCKET_NAME`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`. Reference on [how to set environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
3. Create Google cloud storage bucket and set list, read, write persmission for python script.
4. set environment variables `GCP_BUCKET_NAME` and `GCP_CRED_FILE_PATH`
5. Create virtual environment and install `requirements.txt`
- **Use package without any modifiction**
6. Install package directly from github using command `pip install git+https://github.com/Nik-Jain/sacumen_test.git`
7. To run, from sacumen_test import upload_files
7. Execute upload_files function passing path as a parameter. Path will contain files to be uploaded
- **To Make modifications and generate wheel file for installation**
6. Clone git repo using command `git clone https://github.com/Nik-Jain/sacumen_test.git` and make required changes in scripts and configurations
7. Modify/add unit test cases in `test_sacumen_test.py` file
8. Perform unit testing using command `pytest`
9. If results are as expected, the create distributable whl file using command `python setup.py sdist bdist_wheel`. This will generate whl file in `\dist\`
10. This whl file can be installed using command `pip install <path_to_whl_file>`
11. Execute upload_files function passing path as a parameter. Path will contain files to be uploaded

Example: 
``` python
from sacumen_test import upload_files

upload_files(<path_to_directory>)
```


### Additional Functionality
- This library also can be used for getting all file paths from directory using `get_file_paths()` from helper
- This library also can be used for getting file type from file path using `get_file_extension()` from helper

## Future Enhancements:
- Upload files in a single request instead of request for each file
- UI for setting environment variables & other configurations
