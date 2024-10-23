import os
import subprocess
import time
import config
import logging


def connect():
    os.chdir(config.adb_path)
    connect_result = os.popen(f"adb connect {config.global_adb_port}").read()
    logging.info('Connection result: %s', connect_result)
