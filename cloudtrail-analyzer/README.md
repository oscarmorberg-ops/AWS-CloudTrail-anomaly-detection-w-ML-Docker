# 🚨 CloudTrail Anomaly Scanner

[![CI/CD](https://github.com/oscar-morberg-ops/cloudtrail-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/oscar-morberg-ops/cloudtrail-analyzer/actions)
[![codecov](https://codecov.io/gh/oscar-morberg-ops/cloudtrail-analyzer/branch/master/graph/badge.svg)](https://codecov.io/gh/oscar-morberg-ops/cloudtrail-analyzer)
[![Docker](https://img.shields.io/badge/Docker-Production-blue)](https://hub.docker.com/r/cloudtrail-scanner)

**AWS CloudTrail anomaly detection** med Z-score + Slack alerts + production Docker.

## Features
- 🧮 Z-score anomaly detection (NumPy)
- 📱 Real-time Slack notifications
- 🐳 Multi-stage Docker (50MB alpine)
- ✅ 80% pytest coverage
- 🔒 GitHub Actions CI/CD + CodeQL

## Usage
```bash
python src/main.py --days 7 --threshold 2.0 --slack
