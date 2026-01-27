# NetAnalyzer | IP & Domain Information Tool

A lightweight Python utility to gather geolocation data, ISP details, and network latency for any given IP address or domain name.

## 🚀 Features

* **Smart Resolution:** Automatically detects if the input is an IP address or a domain name (e.g., `google.com`).
* **Geolocation Data:** Fetches City, Region, Country, and Timezone using the ipinfo.io API.
* **ISP Identification:** Displays the organization/ISP owning the IP.
* **Latency Testing:** Performs a real-time ICMP ping test to check responsiveness and round-trip time.

---

## 🛠️ Prerequisites

Before running the script, ensure you have Python 3.x installed and the necessary dependencies.

### 1. Install Dependencies
This script relies on `requests` for API calls and `ping3` for network testing. Install them via pip:

```bash
pip install requests ping3
```

## Getting Started
## Clone the repository:
```bash
git clone https://github.com/RebelFinatic/NetAnalyzer
cd NetAnalyzer
```

## Run the script:

```bash
python netanalyzer.py
```

## Usage: When prompted, enter an IP address (e.g., 8.8.8.8) or a domain (e.g., github.com).
> The following is a sample of what it will look like if you provide a domain like google.com
```bash
Please enter an IP or Domain: google.com

--------IP DETAILS--------

IP: 142.250.190.46
ISP: AS15169 Google LLC
Region: California
City: Mountain View
Timezone: America/Los_Angeles
Country: US
Ping: 12 ms

---------------------------
```
