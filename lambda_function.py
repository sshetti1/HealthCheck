import json
import os
import HealthCheck


def lambda_handler(event, context):
    os.system('export PATH="$/bin:$PATH"')
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
