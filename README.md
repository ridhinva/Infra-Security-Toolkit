# Infra Security Toolkit 🖥️

**6 infrastructure security scanners** — Linux, Windows, Active Directory, Kubernetes, Docker, Cloud.

## Tools

| Tool | Target | Key Checks |
|------|--------|------------|
| `linux_scanner.py` | Linux | SUID/SGID, Writable passwd, Sudo, Kernel exploits |
| `windows_scanner.py` | Windows | Service perms, Unquoted paths, AlwaysInstallElevated |
| `ad_scanner.py` | AD | Kerberoasting, AS-REP, DCSync, ACL abuse |
| `k8s_scanner.py` | Kubernetes | API exposure, Anonymous auth, RBAC |
| `docker_scanner.py` | Docker | Socket access, Privileged mode, API exposure |
| `cloud_scanner.py` | Cloud (AWS/Azure/GCP) | Metadata service, S3 buckets, IMDS |

## Installation

```bash
git clone https://github.com/ridhinva/Infra-Security-Toolkit.git
cd Infra-Security-Toolkit
pip install requests
```

## Usage

```bash
# Linux local privesc check
python3 linux_scanner.py

# K8s API exposure
python3 k8s_scanner.py https://k8s-api:6443

# Cloud metadata
python3 cloud_scanner.py
```

## How Each Scanner Works

### Linux Scanner
Executes locally on a Linux host to identify privilege escalation vectors. Checks for **SUID/SGID binaries** with known exploit vectors (nmap, vim, python, find). Tests if `/etc/passwd` is writable for adding a root user. Runs `sudo -l` to find NOPASSWD entries and command-over-sudo misconfigurations. Identifies running kernel version and matches against public exploit databases.

### Windows Scanner
Scans Windows hosts for common misconfigurations: services with weak permissions (can be started/stopped by non-admin), unquoted service paths (space in path without quotes), AlwaysInstallElevated registry key (allows any user to install MSI as SYSTEM), and registry autologon credentials stored in plaintext.

### AD Scanner
Connects to Active Directory domain controllers and tests for: **Kerberoasting** (request TGS for service accounts), **AS-REP roasting** (accounts without pre-auth), **DCSync** (replicate DC credentials), **ACL abuse** (over-permissioned ACLs on privileged objects), and **NTLM relay** (coerce authentication to attacker).

### K8s Scanner
Probes Kubernetes API server endpoints to detect **unauthenticated access**, **anonymous auth enabled**, and **RBAC misconfigurations**. Checks `/api/v1` for resource listing, `/healthz` for cluster info, and tests for pod creation permissions without auth.

### Docker Scanner
Checks for **Docker socket** (`/var/run/docker.sock`) exposure which allows container escape and host compromise. Tests Docker API (`:2375`) for unauthenticated remote access. Inside containers, checks if running in **privileged mode**, checks capability leaks, and tests for host filesystem mounts.

### Cloud Scanner
Queries cloud provider metadata endpoints to detect **SSRF-exploitable** services. AWS: `169.254.169.254/latest/meta-data/` for instance credentials, user-data for secrets. Azure: IMDS endpoint for managed identity tokens. GCP: metadata server for access tokens and service account info.

## Author

**Ridhin V A** ([@c_y_p_h3r](https://x.com/c_y_p_h3r))


## Disclaimer

For authorized security testing and educational purposes only.
