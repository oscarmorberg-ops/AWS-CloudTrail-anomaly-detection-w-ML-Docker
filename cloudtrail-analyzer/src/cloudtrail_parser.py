import boto3
import json
from datetime import datetime

def get_cloudtrail_events(days=7):
    client = boto3.client('logs', region_name='eu-north-1')
    logs = client.filter_log_events(
        logGroupName='/aws/events/cloudtrail',
        startTime=int((datetime.now().timestamp() - days*86400)*1000)
    )['events']
    return [json.loads(e['message']) for e in logs]
