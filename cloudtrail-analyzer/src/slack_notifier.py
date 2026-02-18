import requests
import os
from src.cloudtrail_anomaly import detect_anomalies

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK", "https://hooks.slack.com/services/FAKE/FAKE/FAKE")

def send_slack_alert(anomalies):
    if not anomalies:
        return
    message = f"🚨 *{len(anomalies)} CloudTrail anomalier!*"
    for anomaly in anomalies[:3]:
        message += f"• {anomaly.get('eventName', 'unknown')}"
    
    response = requests.post(SLACK_WEBHOOK, json={"text": message})
    print(f"Slack: {response.status_code}")

if __name__ == "__main__":
    anomalies = detect_anomalies()
    send_slack_alert(anomalies)
