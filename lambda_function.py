import json
import os
import HealthCheck


def lambda_handler(event, context):
    return HealthCheck.main()
