# ETL pipeline: Extract from csv->Transform to json->Load on MongoDB
import os
import sys

from dotenv import load_dotenv #used to call environment variables 
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi  #used to make a secure http connection 
ca = certifi.where()   #ca - certificate authority

import pandas as pd
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop = True,inplace = True)
            records = data.to_dict(orient='records')
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile = ca)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

""" 
if __name__ == '__main__':
    FILE_PATH = "Network_data\phisingData.csv"
    DATABASE = "ARYAN"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path = FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_to_mongodb(records,DATABASE,Collection)
    print(no_of_records)
"""

