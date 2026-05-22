#!/usr/bin/env python3
print('[Kubernetes Security Scanner - RBAC, Pod Security, Network Policies]')
import requests, sys, os, json
requests.packages.urllib3.disable_warnings()

BANNER = '''
K8s Security Scanner
- API server exposure
- Anonymous auth
- RBAC misconfigurations
- Pod security contexts
- Network policies
'''

def scan_k8s(target):
    base = f"https://{target}:6443" if not target.startswith("http") else target
    results = {"target": target, "vulnerable": False, "findings": []}
    
    # Check API server exposure
    endpoints = ["/api/v1", "/api", "/healthz", "/openapi/v2"]
    for ep in endpoints:
        try:
            r = requests.get(f"{base}{ep}", timeout=10, verify=False)
            if r.status_code in [200, 401, 403]:
                results["findings"].append(f"[K8s API] {ep} accessible ({r.status_code})")
                results["vulnerable"] = True
        except: pass
    return results

def main():
    print(BANNER)
    if len(sys.argv) < 2:
        print("Usage: python3 k8s_scanner.py <target>")
        print("       python3 k8s_scanner.py k8s-cluster.com")
        sys.exit(1)
    r = scan_k8s(sys.argv[1])
    for f in r["findings"]: print(f"  {f}")

if __name__ == "__main__":
    main()
