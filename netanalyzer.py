import requests
import socket
import ipaddress
from ping3 import ping, verbose_ping

def get_isp_from_ip(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = response.json()
        city = data.get('city', 'City not found')
        region = data.get('region', 'Region not found')
        timezone = data.get('timezone', 'Timezone not found')
        country = data.get('country', 'Country not found')
        org = data.get('org', 'ISP not found')
        latency = round(ping(ip) * 1000)

        print(f"\n--------IP DETAILS--------\n")
        print(f"IP: {ip}")
        print(f"ISP: {org}")
        print(f"Region: {region}")
        print(f"City: {city}")
        print(f"Timezone: {timezone}")
        print(f"Country: {country}")
        print(f"Ping: {latency} ms")
        print(f"\n---------------------------")

    except requests.RequestException as e:
        return f'Error: {e}'
    
def check(ip):
    try:
        ipaddress.ip_address(ip)
        get_isp_from_ip(ip)
    except ValueError:
        domain_to_ip = socket.gethostbyname(ip)
        get_isp_from_ip(domain_to_ip)

ip_or_domain = input("Please enter an IP or Domain: ")
check(ip_or_domain)
