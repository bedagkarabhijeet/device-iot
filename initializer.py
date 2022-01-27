

import json
import boto3
import os

from Utilities.Logger.logger import LogBuilder


def configuration():
    try:

        if os.environ.get('CONFIG_BUCKET'):
            s3 = boto3.resource('s3')
            content_object = s3.Object(os.environ['CONFIG_BUCKET'], 'config.json')
            file_content = content_object.get()['Body'].read().decode('utf-8')
            return json.loads(file_content)

        with open("config.json") as config:
            return json.loads(config.read())
    except Exception as e:
        raise Exception(f"Failed while reading configuration {e}")


configuration = configuration()

logger = LogBuilder\
    .set_log_level()\
    .enable_stdout()\
    .get()
