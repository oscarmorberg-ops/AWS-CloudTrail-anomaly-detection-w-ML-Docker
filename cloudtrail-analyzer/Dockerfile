# Build stage (HELA ekosystemet)
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Production (minimal 50MB image)
FROM python:3.12-alpine
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY src/ ./src/
EXPOSE 8080
CMD ["python", "-m", "src.cloudtrail_anomaly"]
