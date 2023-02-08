from setuptools import setup

# This file is getting used for create whl file of sacumen_test package. 
# To create whl file, use command "python setup.py sdist bdist_wheel 

setup(name='sacumen_test',
      version='0.1.0',
      description='This package is a solution to upload files to aws and google cloud storage based on file type',
      author='Nikhil Jain',
      author_email='jainnikhil025@gmail.com',
      packages=['sacumen_test'],
      install_requires=[
        'google-api-core==2.11.0',
        'google-auth==2.16.0',
        'google-cloud-core==2.3.2',
        'google-cloud-storage==2.7.0',
        'google-crc32c==1.5.0',
        'google-resumable-media==2.4.1',
        'googleapis-common-protos==1.58.0',
        'boto3',
        ]
      )