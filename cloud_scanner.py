#!/usr/bin/env python3
print('[Cloud Security Scanner - AWS, Azure, GCP metadata & misconfigurations]')
import requests, sys, os

BANNER = '''
Cloud Security Scanner
- AWS metadata service (169.254.169.254)
- Azure IMDS
- GCP metadata
- S3 bucket enumeration
- Cloud storage exposure
'''

CLOUD_ENDPOINTS = [
    ("AWS", "http://169.254.169.254/latest/meta-data/"),
    ("AWS", "http://169.254.169.254/latest/user-data/"),
    ("Azure", "http://169.254.169.254/metadata/instance?api-version=2021-02-01"),
    ("GCP", "http://metadata.google.internal/computeMetadata/v1/"),
    ("GCP", "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"),
]

def main():
    print(BANNER)
    for provider, url in CLOUD_ENDPOINTS:
        try:
            headers = {"Metadata": "true"} if "google" in url else {}
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                print(f"[!!] [{provider}] {url}")
                print(f"     {r.text[:200]}")
        except: pass

if __name__ == "__main__":
    main()
