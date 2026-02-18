import json, boto3, numpy as np
import sys
sys.path.append('src/ml')
from advanced_features import extract_pro_features, features_to_vector

sns = boto3.client('sns')

def lambda_handler(event, context):
    features = extract_pro_features(event['detail'])
    feature_vector = features_to_vector(features)
    
    # Proffs Z-score (28 features)
    z_scores = np.abs(np.array(feature_vector) - 0.5) / 0.2
    anomaly_score = float(np.max(z_scores))
    
    if anomaly_score > 3.0:
        sns.publish(
            TopicArn='arn:aws:sns:eu-north-1:695210052267:critical-anomalies',
            Subject=f"🚨 PRO Anomaly: {event['detail']['eventName']}",
            Message=f"Score: {anomaly_score:.2f} | IP: {event['detail']['sourceIPAddress']}"
        )
    
    return {'statusCode': 200, 'body': json.dumps({'anomaly_score': anomaly_score})}
