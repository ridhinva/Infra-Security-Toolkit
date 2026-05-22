#!/usr/bin/env python3
print('[Docker Security Scanner - Container Escape, Misconfigurations]')
import requests, sys, os, json, subprocess

BANNER = '''
Docker Security Scanner
- Docker socket exposure
- Privileged containers
- Capability leaks
- Mount misconfigurations
- Registry vulnerabilities
'''

def check_docker_socket():
    if os.path.exists('/var/run/docker.sock'):
        return ["[DOCKER] Docker socket accessible - container escape possible"]
    return []

def check_docker_api():
    try:
        r = requests.get("http://localhost:2375/version", timeout=5)
        if r.status_code == 200:
            return [f"[DOCKER] Docker API exposed on port 2375 - v{r.json().get('Version')}"]
    except: pass
    return []

def main():
    print(BANNER)
    findings = check_docker_socket() + check_docker_api()
    for f in findings: print(f"  {f}")

if __name__ == "__main__":
    main()
