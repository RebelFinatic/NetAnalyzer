import requests
import socket
import ipaddress
import sys
import re
from ping3 import ping, verbose_ping

# Gathers relevant information from an ip address
def get_isp_from_ip(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = response.json()
        city = data.get('city', 'City not found')
        region = data.get('region', 'Region not found')
        timezone = data.get('timezone', 'Timezone not found')
        country = data.get('country', 'Country not found')
        org = data.get('org', 'ISP not found')
        
        # Performs latency test, if failed it assumes that ICMP is disabled
        latency = ping(ip)
        if latency is not None:
            latency = round(latency * 1000)
            latency = str(latency) + " ms"
        else:
            latency = 'ICMP may be disabled (Ping Test Failed)'

        print(f"\n--------IP DETAILS--------\n")
        print(f"IP: {ip}")
        print(f"ISP: {org}")
        print(f"Region: {region}")
        print(f"City: {city}")
        print(f"Timezone: {timezone}")
        print(f"Country: {country}")
        print(f"Ping: {latency}")
        print(f"\n---------------------------")

    except requests.RequestException as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')
    
# Check if ip is valid if not assume its a domain
def check(ip):
    try:
        ipaddress.ip_address(ip)
        get_isp_from_ip(ip)
    except ValueError:
        try:
            domain_to_ip = socket.gethostbyname(ip)
            get_isp_from_ip(domain_to_ip)
        except socket.gaierror as e:
            print(f'Error resolving domain: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

if len(sys.argv) == 2: # Check if user has passed a domain/ip as argument
    ip_or_domain = sys.argv[1]
    drop_prefix = re.sub(r'^https?://', '', ip_or_domain)
    check(drop_prefix)  
else:
    ip_or_domain = input("Please enter an IP or Domain: ")
    drop_prefix = re.sub(r'^https?://', '', ip_or_domain)
    check(drop_prefix)  


