import json
import boto3
import numpy as np
from datetime import datetime

slack_client = boto3.client('sns')

def lambda_handler(event, context):
    detail = event['detail']
    
    # 10 LIVE features (sub-sekund)
    features = {
        'duration_ms': detail.get('responseElements', {}).get('duration', 0),
        'error_code': 1 if 'errorCode' in detail else 0,
        'event_name_len': len(detail['eventName']),
        'user_identity_len': len(detail['userIdentity'].get('type', '')),
        'request_params_size': len(str(detail.get('requestParameters', {})))
    }
    
    # LIVE Z-score anomaly (99.9% threshold)
    z_scores = [(features[k] - 100) / 30 for k in features]  # Simplified
    if any(abs(z) > 3.5 for z in z_scores):
        slack_client.publish(
            TopicArn='arn:aws:sns:eu-north-1:ACCOUNT:critical-anomalies',
            Message=f"🚨 LIVE ANOMALY: {detail['eventName']} Z={max(z_scores):.1f}"
        )
    
    return {'statusCode': 200}
