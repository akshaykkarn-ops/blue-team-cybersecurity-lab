# Blue Team Cybersecurity Lab 🛡️

Role Target: **SOC Analyst / Security Operations (Blue Team)**

This project demonstrates hands-on defensive cybersecurity skills through
network traffic analysis, firewall hardening, and vulnerability management
using industry-standard tools on Kali Linux.

---

## 🎯 Objective
To simulate real-world Blue Team / SOC analyst workflows by:
- Monitoring live network traffic
- Enforcing host-based firewall rules
- Identifying vulnerabilities using OpenVAS
- Troubleshooting security tooling failures

---

## 🧰 Tools & Technologies
- **Operating System:** Kali Linux (VMware)
- **Packet Analysis:** Python, Scapy
- **Firewall:** iptables (netfilter)
- **Vulnerability Scanner:** OpenVAS / Greenbone Vulnerability Manager (GVM)
- **Services:** Redis, ospd-openvas, gvmd, gsad

---

## 🔍 Project Modules

### 1️⃣ Packet Sniffing & Traffic Analysis
- Captured 100 live packets using Scapy
- Identified TCP, UDP, and ICMP traffic
- Generated protocol distribution bar chart
- Analyzed normal system traffic patterns

### 2️⃣ Firewall Configuration (iptables)
- Implemented default-deny firewall policy
- Allowed only:
  - Loopback traffic
  - ESTABLISHED / RELATED connections
  - SSH (22)
  - HTTP (80)
- Verified firewall behavior through SSH testing

### 3️⃣ Vulnerability Scanning (OpenVAS)
- Installed and configured OpenVAS (GVM)
- Executed a full vulnerability scan on localhost
- Analyzed CVSS severity and remediation guidance

---

## 🛠️ Troubleshooting & Challenges
This project involved resolving real-world security tool failures:
- Disk exhaustion breaking OpenVAS database creation
- PostgreSQL cluster initialization issues
- Feed synchronization locks
- Greyed-out scan configurations
- Service dependency failures (Redis, OSPD, GVMD, GSAD)

All issues were resolved through systematic troubleshooting,
disk resizing, feed re-synchronization, and service validation.

---

## 📄 Documentation
A full 2–3 page lab report is included with:
- Commands used
- Screenshots
- Results analysis
- Key learnings

📁 `report/Final_Cybersecurity_Lab_Report_Extended.pdf`

---

## 🚀 Key Skills Demonstrated
- Network traffic analysis
- Linux firewall hardening
- Vulnerability management
- SOC-style troubleshooting
- Defensive security mindset

---
## Author
**Akshay** 
Aspiring SOC Analyst / Blue Team Practitioner

## 👤 Author
**Akshay**  
Aspiring SOC Analyst / Blue Team Practitioner
