import numpy as np
from src.cloudtrail_parser import get_cloudtrail_events

def detect_anomalies():
    events = get_cloudtrail_events(days=1)
    durations = [e.get('duration_ms', 0) for e in events]
    
    # Z-SCORE HELVETE (kopiera, testa thresholds)
    z_scores = np.abs(np.zscore(durations))
    anomalies = [e for i, e in enumerate(events) if z_scores[i] > 2.0]
    
    print(f"🚨 {len(anomalies)} anomalies hittade!")
    return anomalies
