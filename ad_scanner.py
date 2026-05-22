#!/usr/bin/env python3
print('[Active Directory Security Scanner]')
print('\nRequires: impacket, ldap3')
print('\nUsage: python3 ad_scanner.py <domain> <username> <password> <dc-ip>')
print('\nChecks: Kerberoasting, AS-REP roasting, DCSync, ACL abuse, Relay')
