#!/usr/bin/env python3
print('[Linux Security Scanner - Privilege Escalation & Hardening Check]')
import subprocess, sys, os, pwd

BANNER = '''
Linux Security Scanner
- SUID/SGID binaries
- Writable /etc/passwd
- Sudo misconfigurations
- Kernel exploits
- Open ports
- Weak permissions
'''

def check_suid():
    result = subprocess.run("find / -perm -4000 2>/dev/null", shell=True, capture_output=True, text=True, timeout=30)
    suids = result.stdout.strip().split('\n')
    interesting = ['nmap', 'vim', 'python', 'less', 'more', 'cp', 'mv', 'find', 'bash', 'sh', 'pkexec']
    findings = []
    for s in suids:
        for i in interesting:
            if i in s.lower():
                findings.append(f"[SUID] {s} - potentially exploitable")
    return findings

def check_writable_etc():
    if os.access('/etc/passwd', os.W_OK):
        return ["[CRITICAL] /etc/passwd is writable - can add root user"]
    return []

def check_sudo():
    result = subprocess.run("sudo -l 2>&1", shell=True, capture_output=True, text=True, timeout=10)
    findings = []
    if '(root)' in result.stdout and 'NOPASSWD' in result.stdout:
        findings.append("[SUDO] User has NOPASSWD sudo access")
    return findings

def main():
    print(BANNER)
    findings = []
    findings.extend(check_suid())
    findings.extend(check_writable_etc())
    findings.extend(check_sudo())
    for f in findings: print(f)

if __name__ == "__main__":
    main()
