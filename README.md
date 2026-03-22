# AWS CloudTrail Anomaly Detection with ML + Docker

End‑to‑end pipeline that ingests AWS CloudTrail logs, runs ML‑based anomaly detection and scans EC2 security posture – all containerized with Docker and wired to GitHub Actions CI/CD.

## 🚀 Live components

- `cloudtrail-analyzer` – ML anomaly detection on CloudTrail API activity (e.g. rare actions, unusual identities).
- `ec2_scanner.py` – CCSIO EC2 Security Scanner v2 for misconfigurations and insecure instances.
- GitHub Actions workflows – production pipeline for building and running the analyzers on every push.
- Docker image – packaged for easy deploy to your own environment.

## 🔑 Key features

- ML-based anomaly detection on CloudTrail API activity (rare actions, unusual identities, abnormal patterns over time).
- Automated EC2 security posture scanning to catch misconfigurations and insecure instances early.
- Fully containerized with Docker and wired into GitHub Actions CI/CD for repeatable, production-like runs on every push.

## 🏃 Quickstart (local demo)

```bash
# Clone repo
git clone https://github.com/oscarmorberg-ops/AWS-CloudTrail-anomaly-detection-w-ML-Docker.git
cd AWS-CloudTrail-anomaly-detection-w-ML-Docker

# Build Docker image
docker build -t cloudtrail-ml .

# Run CloudTrail analyzer (mount your CloudTrail JSON logs)
docker run -v /path/to/cloudtrail:/data cloudtrail-ml python cloudtrail-analyzer/analyze.py /data

# Run EC2 security scanner
python3 ec2_scanner.py
```

## 🎯 What this is for

This project is my lab for combining CloudTrail threat hunting with ML anomaly detection and automated EC2 security scanning, as preparation for real‑world cloud security engineering work.

## 🔗 Related projects

- **CCISO Dashboard v3** – central dashboard where CloudTrail anomalies, S3 posture and GuardDuty findings are visualized together.
- **GuardDuty ML v8.0** – live GuardDuty findings pipeline that enriches, scores and forwards alerts into the dashboard.
- **AWS S3 Enterprise Hardening v7.0** – opinionated S3 security posture tooling used in the same lab environment.
