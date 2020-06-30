#/usr/bin/python

#[START imports]
import logging
import os
from google.cloud import storage
from io import BytesIO
 
class readWriteList:
    
    client = storage.Client.from_service_account_json("/home/dwarika/Learning/GCP/storage.json")
    bucket = client.get_bucket("readwrite")
        
    def _init__(self):
        pass
        readWriteList.client = storage.Client.from_service_account_json("/home/dwarika/Learning/GCP/storage.json")
        bucket = readWriteList.client.get_bucket("readwrite")     
    
    def __uploadFiles(self):
        filename = "sample" #"%s/%s" % ('',"datas.txt")
        blob = readWriteList.bucket.blob(filename)
        
        with open('/home/dwarika/Learning/GCP/storage/action/data.txt', 'rb') as f:
            blob.upload_from_file(f)
        print("Upload complete")    
        
    def __listBucketFiles(self):
        filename = list(readWriteList.bucket.list_blobs())
        for name in filename:
            print(name)
    
    def __readFile(self):
        #read = readWriteList.bucket.blob("readwrite")
        blob = readWriteList.bucket.blob("sample")
        data = blob.download_as_string().decode("utf-8")
        
        print(data)