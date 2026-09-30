import pandas as pd
import requests
import boto3
import json

# ==============================================================================
# DANGER: HARDCODED CREDENTIALS (Intentionally left for local testing)
# TODO: Move these to environment variables or a secure vault before production merge!
# ==============================================================================

# AWS Access Credentials (Triggers GitHub Secret Scanning)
AWS_ACCESS_KEY_ID = "AKIA52GPOB7ABCDEXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# External API Token 
THREAT_INTEL_API_TOKEN = "ghp_DemoTokenForSecurityScanAlerts123456"

def fetch_cloud_logs(bucket_name, file_key):
    """Simulates fetching access logs from an S3 bucket."""
    print(f"Connecting to S3 bucket: {bucket_name}...")
    
    # Initialize connection using the hardcoded credentials
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    
    print(f"Successfully downloaded {file_key}.")
    # Simulating a dataframe creation from the logs
    dummy_data = {'timestamp': ['2026-10-01 12:00:00'], 'source_ip': ['192.168.1.50'], 'status': [200]}
    return pd.DataFrame(dummy_data)

def analyze_traffic(dataframe, api_endpoint):
    """Sends the processed logs to an external API using the vulnerable requests library."""
    print("Formatting log data for threat analysis...")
    payload = dataframe.to_json(orient='records')
    
    headers = {
        "Authorization": f"Bearer {THREAT_INTEL_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    print("Transmitting to threat intelligence endpoint...")
    # This call uses the vulnerable requests library specified in requirements.txt
    try:
        response = requests.post(api_endpoint, headers=headers, data=payload, timeout=5)
        return response.status_code
    except Exception as e:
        print("API connection simulated/failed.")
        return None

if __name__ == "__main__":
    print("Starting traffic anomaly pipeline...")
    
    # Step 1: Fetch the logs
    df_logs = fetch_cloud_logs("corp-prod-traffic-logs", "access_log_1001.csv")
    
    # Step 2: Analyze the logs
    status = analyze_traffic(df_logs, "https://api.threatintel-demo.com/v1/analyze")
    
    print("Pipeline execution complete.")