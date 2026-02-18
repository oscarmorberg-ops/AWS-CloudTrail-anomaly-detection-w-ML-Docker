import numpy as np
from math import log2
from collections import Counter

def entropy(ip):
    chars = [c for c in ip if c.isdigit()]
    if len(chars) == 0:
        return 0
    counts = Counter(chars)
    return -sum((count/len(chars)) * log2(count/len(chars)) for count in counts.values())

def extract_pro_features(event):
    return {
        'ip_entropy': entropy(event.get('sourceIPAddress', '')),
        'arn_depth': len(str(event.get('requestParameters', {}).get('arn', '')).split('/')),
        'request_size': len(str(event.get('requestParameters', {}))),
        'event_name_len': len(event.get('eventName', '')),
        'useragent_len': len(event.get('userAgent', '').split()),
        'has_error': 1 if event.get('errorCode') else 0,
        'cross_account': 1 if 'AssumeRole' in str(event.get('eventName', '')) else 0,
        'suspicious_event': 1 if event.get('eventName') in ['RunInstances', 'CreateKey'] else 0
    }

def features_to_vector(features):
    """28 features vector för ML"""
    vector = list(features.values()) + [0.0] * (28 - len(features))
    return vector[:28]
