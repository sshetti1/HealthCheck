import json
import os
from time import sleep

import HealthCheck


def lambda_handler(event, context):
    HealthCheck.main()
    status = "Done"
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Health Check for " + os.getenv('USERNAME'): status
        })
    }
