# NetAnalyzer | IP & Domain Information Tool

A lightweight Python utility to gather geolocation data, ISP details, and network latency for any given IP address or domain name.

## 🚀 Features

* **Smart Resolution:** Automatically detects if the input is an IP address or a domain name (e.g., `google.com`).
* **Geolocation Data:** Fetches City, Region, Country, and Timezone using the ipinfo.io API.
* **ISP Identification:** Displays the organization/ISP owning the IP.
* **Latency Testing:** Performs a real-time ICMP ping test to check responsiveness and round-trip time.
* **Configurable Timeout:** Customize ping timeout duration via command-line arguments.
* **Version Info:** Check the current script version with `--version` flag.

---

## 🛠️ Prerequisites

Before running the script, ensure you have Python 3.x installed and the necessary dependencies.

### Install Dependencies
This script relies on `requests` for API calls and `ping3` for network testing. Install them via pip:
```bash
pip install requests ping3
```

## Getting Started

### Clone the repository:
```bash
git clone https://github.com/RebelFinatic/NetAnalyzer
cd NetAnalyzer
```

## Usage

### Basic Usage
Analyze an IP address or domain:
```bash
python netanalyzer.py 8.8.8.8
python netanalyzer.py google.com
```

### Custom Timeout
Set a custom ping timeout (in seconds):
```bash
python netanalyzer.py google.com --timeout 2
```

### Check Version
Display the current script version:
```bash
python netanalyzer.py --version
```

### Help
View all available options:
```bash
python netanalyzer.py --help
```

## Example Output
```bash
python netanalyzer.py google.com

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

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `target` | IP address or domain to analyze | Required |
| `--timeout` | Ping timeout duration in seconds | 4 |
| `--version` | Show script version | - |
| `--help` | Display help message | - |