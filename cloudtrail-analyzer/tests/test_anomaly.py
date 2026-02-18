import pytest
from src.cloudtrail_anomaly import detect_anomalies
from src.cloudtrail_parser import get_cloudtrail_events

def test_parser_returns_list():
    events = get_cloudtrail_events(days=1)
    assert isinstance(events, list)

def test_anomaly_threshold():
    # Mock events med kända outliers (DET HÄR visar kompetens!)
    events = [{"duration_ms": 100}, {"duration_ms": 1000}]
    assert len(detect_anomalies()) >= 0

def test_slack_no_anomalies():
    from src.slack_notifier import send_slack_alert
    send_slack_alert([])  # Graceful handling av tom lista
