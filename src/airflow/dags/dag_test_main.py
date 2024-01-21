# dags/main.py
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import argparse
import calendar
from airflow.sensors.filesystem import FileSensor
from import_for_dags import *
from src.tools.airflow_sensors import FileSensorWithMask
import os
import glob
import shutil

from src.tools.parser import CSVParser
from src.tools.sql import DBConnector

file_sensing_task = FileSensor(task_id='sense_the_csv',
                                   filepath=INCOMING_MESSAGES_PATH + '/*_CSV_LOAD_*.csv',
                                   poke_interval=10)

def findCSVLoadFile(ti):
    print(f"Start to search files in incoming folder")
    files = glob.glob(INCOMING_MESSAGES_PATH + '/*_CSV_LOAD_*.csv')
    files.sort(key = os.path.getmtime)#TODO Remake this sort
    print(files)
    ti.xcom_push(key='csv_file_name', value=files[0])

def step2(ti):
    print(f"Start to take data from a file and load in DB")
    file_name = ti.xcom_pull(key='csv_file_name')
    print(file_name)
    csvParser = CSVParser()
    csvParser.parse_csv_file(file_name, ',')
    messageDict = csvParser.get_message()
    print("Loading to DB...")
    dbConn = DBConnector()
    dbConn.call_sp_ins_account(messageDict['AccountId'], messageDict['AccountName'], messageDict['AccountDescription'], messageDict['Currency'])
    #TODO DB load process

def step3(ti):
    print(f"Moving file to processed folder")
    file_name = ti.xcom_pull(key='csv_file_name')
    shutil.move(file_name, file_name.replace('/incoming/', '/processed/'))




if __name__ == "__main__":
    pass