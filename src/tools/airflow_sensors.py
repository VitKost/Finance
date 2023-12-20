"""
Parameters:
 sql: str, sql to execute
Sensor class for snowflake
"""
import datetime
import os
from glob import glob
from typing import Sequence

from airflow.hooks.filesystem import FSHook
from airflow.sensors.base import BaseSensorOperator
from airflow.utils.context import Context

class FileSensorWithMask(BaseSensorOperator):
    def __init__(self, *, filepath, fs_conn_id="fs_default", recursive=False, **kwargs):
        super().__init__(**kwargs)
        self.filepath = filepath
        self.fs_conn_id = fs_conn_id
        self.recursive = recursive
        self.found_file_path = ''

    def poke(self, context: Context):
        hook = FSHook(self.fs_conn_id)
        basepath = hook.get_path()
        full_path = os.path.join(basepath, self.filepath)
        self.log.info("Poking for file %s", full_path)

        for path in glob(full_path, recursive=self.recursive):
            if os.path.isfile(path):
                mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y%m%d%H%M%S")
                self.log.info("Found File %s last modified: %s", path, mod_time)
                self.found_file_path = path
                self.filepath = path
                self.log.info("File is %s", self.found_file_path)
                return True

            for _, _, files in os.walk(path):
                if files:
                    return True
        return False
