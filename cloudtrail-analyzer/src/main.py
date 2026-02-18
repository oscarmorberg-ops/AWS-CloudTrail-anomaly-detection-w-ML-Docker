#!/usr/bin/env python3
"""CloudTrail Anomaly Scanner - Production CLI"""
import argparse
import sys
from src.cloudtrail_parser import get_cloudtrail_events
from src.cloudtrail_anomaly import detect_anomalies  
from src.slack_notifier import send_slack_alert

def main():
    parser = argparse.ArgumentParser(description="AWS CloudTrail Anomaly Scanner")
    parser.add_argument("--days", type=int, default=1, help="Days of logs to scan")
    parser.add_argument("--threshold", type=float, default=2.0, help="Z-score threshold")
    parser.add_argument("--slack", action="store_true", help="Send Slack alerts")
    args = parser.parse_args()
    
    print("🔍 Scanning CloudTrail logs...")
    events = get_cloudtrail_events(days=args.days)
    anomalies = detect_anomalies(threshold=args.threshold)
    
    if anomalies:
        print(f"🚨 {len(anomalies)} anomalies hittade!")
        if args.slack:
            send_slack_alert(anomalies)
    else:
        print("✅ No anomalies detected")

if __name__ == "__main__":
    main()
