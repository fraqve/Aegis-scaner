# Aegis-Scan
> A modular CLI security scanner combining active reconnaissance with threat intelligence enrichment and AI-powered analysis.

---

## Overview

Aegis-Scan runs nmap, gobuster, and nikto against a target, enriches the findings with VirusTotal and AbuseIPDB reputation data, then sends the full report to Google Gemini for structured security analysis. Output is saved to two files: a raw master report and an AI-generated assessment.

---

## Features

- **Network scanning** — Service and version detection via Nmap (`-sV`)
- **Directory enumeration** — Web path discovery via Gobuster
- **Web vulnerability scanning** — Header and misconfiguration checks via Nikto
- **Threat intelligence enrichment** — IP reputation via VirusTotal and AbuseIPDB
- **AI-assisted analysis** — Structured security assessment via Google Gemini
- **Modular architecture** — Separate modules for scanning, analysis, and reporting

---

## Requirements

- Python 3.8+
- Nmap, Nikto, Gobuster installed and available on PATH
- API keys for VirusTotal, AbuseIPDB, and Google Gemini
- Wordlist for Gobuster (default: `/usr/share/seclists/common.txt`)

---

## Installation
```bash
git clone https://github.com/fraqve/Aegis-scan.git
cd Aegis-scaner
pip install -r requirements.txt
# Add your API keys to config.json
```

---

## Usage
```bash
# Basic scan
python main.py --target 192.168.1.1

# Custom wordlist
python main.py --target 192.168.1.1 --wordlist /path/to/wordlist
```

**Output:**
- `report.txt` — Master report with all scan and enrichment data
- `gemini_report.txt` — AI-generated security assessment

---

## Project Structure
```
Aegis-scan/
├── main.py          # Entry point and CLI argument handling
├── scan.py          # Nmap, Gobuster, Nikto wrappers
├── analysis.py      # VirusTotal, AbuseIPDB, and Gemini integrations
├── report.py        # Report generation and output formatting
├── config.json      # API keys — not tracked by git
├── config.json  # Template for API key configuration
└── requirements.txt
```

---

## Tech Stack

- **Python 3** — Core language
- **subprocess** — Nmap, Gobuster, Nikto execution
- **requests** — API communication
- **VirusTotal API v3** — IP reputation and verdict data
- **AbuseIPDB API v2** — IP abuse confidence scoring
- **Google Gemini API** — AI-powered security analysis

---

## Status

Phase 1 (scanning and reporting) complete. Phase 2 (threat intelligence enrichment and AI analysis) complete.

---

## Disclaimer

This tool is intended for authorized security assessments and educational purposes only. Always obtain proper permission before scanning any network or system you do not own.

---

## Demo

**Running the scanner:**
![Running](Proof%20of%20work/project_running.png)

**Master report output:**
![Report](Proof%20of%20work/report.png)

**Gemini AI analysis:**
![Gemini Report](Proof%20of%20work/gemini_report.png)
