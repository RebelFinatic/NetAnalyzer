import requests
import socket
import ipaddress
import sys
import re
import argparse
from ping3 import ping, verbose_ping

__version__ = "1.0.0"

# Gathers relevant information from an ip address
def get_isp_from_ip(ip, timeout=4):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = response.json()
        city = data.get('city', 'City not found')
        region = data.get('region', 'Region not found')
        timezone = data.get('timezone', 'Timezone not found')
        country = data.get('country', 'Country not found')
        org = data.get('org', 'ISP not found')
        
        # Performs latency test, if failed it assumes that ICMP is disabled
        latency = ping(ip, timeout=timeout)
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
def check(ip, timeout=4):
    try:
        ipaddress.ip_address(ip)
        get_isp_from_ip(ip, timeout)
    except ValueError:
        try:
            domain_to_ip = socket.gethostbyname(ip)
            get_isp_from_ip(domain_to_ip, timeout)
        except socket.gaierror as e:
            print(f'Error resolving domain: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='python netanalyzer.py',
        description='Analyze IP addresses or domains'
    )
    parser.add_argument('target', nargs='?', help='IP address or domain to analyze')
    parser.add_argument('--timeout', type=int, default=4, help='Ping timeout in seconds (default: 4)')
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    
    args = parser.parse_args()
    
    if not args.target:
        parser.print_help()
        sys.exit(1)
    
    drop_prefix = re.sub(r'^https?://', '', args.target)
    check(drop_prefix, args.timeout)