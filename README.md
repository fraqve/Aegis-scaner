# Aegis-Scaner

> A Python-based CLI security scanner for network reconnaissance and threat intelligence enrichment.

---

## Overview

Aegis-Scaner is a modular command-line security tool built for blue team workflows. It combines active network scanning with threat intelligence APIs to help analysts quickly assess hosts, identify open services, and enrich findings with reputation data.

---

## Features

- **Network scanning** — Host discovery and service detection via Nmap (`-sV`)
- **Threat intelligence enrichment** — IP and file reputation lookups via VirusTotal and AbuseIPDB
- **AI-assisted analysis** — Automated finding summarization via Google Gemini API
- **Structured reporting** — Clean, readable output saved to report files
- **Modular architecture** — Separate modules for scanning, analysis, and reporting

---

## Installation

**Requirements**

- Python 3.8+
- Nmap, Nikto, Gobuster installed on your system
- API keys for VirusTotal, AbuseIPDB, and Google Gemini

**Steps**

```bash
# Clone the repository
git clone https://github.com/fraqve/Aegis-scaner.git
cd Aegis-scaner

# Install dependencies
pip install -r requirements.txt

# Configure API keys edit config.json and add your API keys

---

## Usage

```bash
# Basic scan
python main.py --target 192.168.1.1

# Provide the wordlist for gobuster default is /usr/share/seclists/common.txt
python main.py --target 192.168.1.1 --wordlist /path/to/wordlist
```

---

## Project Structure

```
Aegis-scaner/
├── main.py          # Entry point and CLI argument handling
├── scan.py          # Nmap wrapper and network scanning logic
├── analysis.py      # Threat intelligence API integrations
├── report.py        # Output formatting and report generation
├── config.json      # API keys and configuration (not tracked)
└── requirements.txt
```

---

## Tech Stack

- **Python 3** — Core language
- **subprocess (to use the tools)** — Nmap, Gobuster, Nikto
- **requests** — API communication
- **VirusTotal API** — File and IP reputation
- **AbuseIPDB API** — IP abuse confidence scoring
- **Google Gemini API** — AI-powered finding analysis

---

## Status

Actively in development.

**Phase 1 (scanning and reporting)** complete.

**Phase 2 (analysis)** in progress:

  -**Virus total api** Done.
  
  -**Abuseipdb** in progress.
  
  -**Gemini ai analysis** in progress.

---

## Disclaimer

This tool is intended for authorized security assessments and educational purposes only. Always obtain proper permission before scanning any network or system you do not own.
