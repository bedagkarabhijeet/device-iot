

import json
import boto3
import os

from Utilities.Logger.logger import LogBuilder


def configuration():
    with open("config.json") as config:
        return json.loads(config.read())


configuration = configuration()

logger = LogBuilder\
    .set_log_level()\
    .enable_stdout()\
    .get()
