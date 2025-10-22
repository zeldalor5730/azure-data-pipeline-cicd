import json, requests, os

def send_metric(metric_name, value):
    log_analytics_workspace = os.getenv("LOG_ANALYTICS_WORKSPACE")
    payload = {"metric": metric_name, "value": value}
    requests.post(f"{log_analytics_workspace}/metrics", data=json.dumps(payload))
    print(f"📈 Sent metric: {metric_name}={value}")

if __name__ == "__main__":
    send_metric("spark_job_runtime_sec", 230)
