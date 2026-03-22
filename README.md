# AWS CloudTrail Anomaly Detection with ML + Docker

End‑to‑end pipeline that ingests AWS CloudTrail logs, runs ML‑based anomaly detection and scans EC2 security posture – all containerized with Docker and wired to GitHub Actions CI/CD. [web:1004][web:1005]

## 🚀 Live components

- `cloudtrail-analyzer` – ML anomaly detection on CloudTrail API activity (e.g. rare actions, unusual identities). [web:1004][web:1005]
- `ec2_scanner.py` – CCSIO EC2 Security Scanner v2 for misconfigurations and insecure instances. [web:1012][web:1018]
- GitHub Actions workflows – production pipeline for building and running the analyzers on every push. [web:1009][web:1011]
- Docker image – packaged for easy deploy to your own environment. [web:1009]

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

This project is my lab for combining CloudTrail threat hunting with ML anomaly detection and automated EC2 security scanning, as preparation for real‑world cloud security engineering work. [web:1005][web:1013]
