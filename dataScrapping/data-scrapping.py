''' 
This is a funcaitonal file only to download Establishment Registration and Medical Device Listing Files from FDA ; and also can download released 510k zip files from FDA. 
These files are updated monthly on the 5th of each month on fda website, therefore, the system will update on the 6th to make sure the latest info can be used for the text builder.
'''
import json
import requests
import os
import sys
from zipfile import ZipFile
import io
import time

# Configure
INFO_FILE = "fda_database.json"
ZIP_FILES_URL_EST = "zip-files-url" 
ZIP_FILES_URL_510K = "510k-zip-file-url"
ZIP_FILE_URL_PRODUCT_CODE = "product-code-classfication"

DIRECTORY_FOR_EST = "FDA Registration Record/EST"
DIRECTORY_FOR_510K = "FDA Registration Record/510k"
DIRECTORY_FOR_PRODUCTCODE = "FDA Registration Record/PRODUCTCODE"

class data_scrapper_510k(object):
    def __init__(self):
        self.config_json = INFO_FILE
        self.download_url = ZIP_FILES_URL_510K
        self.directory = DIRECTORY_FOR_510K

    def scrap(self):
        with open(os.path.join(sys.path[0],self.config_json), "r") as JSON_FILE:
            data = json.load(JSON_FILE)
            url = data[self.download_url]

        for i in url.keys():
            r = requests.get(url[i], stream = True)
            z = ZipFile(io.BytesIO(r.content))
            z.extractall(self.directory)

class data_scrapper_product_code(object):
    def __init__(self):
        self.config_json = INFO_FILE
        self.download_url = ZIP_FILE_URL_PRODUCT_CODE
        self.directory = DIRECTORY_FOR_PRODUCTCODE
    
    def scrap(self):
        with open(os.path.join(sys.path[0],self.config_json), "r") as JSON_FILE:
            data = json.load(JSON_FILE)
            url = data[self.download_url]
        
        r = requests.get(url, stream = True)
        z = ZipFile(io.BytesIO(r.content))
        z.extractall(self.directory)

if __name__ == "__main__":
    data_scrapper_pc_code = data_scrapper_product_code()
    data_scrapper_pc_code.scrap()
    print('download done!')

