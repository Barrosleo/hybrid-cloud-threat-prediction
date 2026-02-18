# TCP Port Scan — Simulation Steps

This document describes how the TCP port scan traffic was generated and captured for model evaluation.

---

## 1. Objective
To simulate a reconnaissance phase attack (TCP SYN scan) and capture the resulting traffic.

---

## 2. Environment Setup
- **Attacker VM:** Kali Linux  
- **Target VM:** Ubuntu Server  
- **Network:** VirtualBox Host-Only Network  
- **Tools Used:**  
  - `nmap`  
  - Wireshark / tcpdump  

---

## 3. Steps Performed

### **Step 1 — Basic SYN Scan**
```bash
sudo nmap -sS <target-ip>
Step 2 — Aggressive Scan
bash
sudo nmap -A -T4 <target-ip>
Step 3 — Capture traffic
bash
sudo tcpdump -i eth0 tcp -w tcp_scan.pcap
Step 4 — Extract flow features
Using CICFlowMeter or custom Python scripts.
```
## 4. Observed Characteristics
Repeated SYN packets to sequential ports

Low packet payload

High connection attempt rate

Typical reconnaissance signature

## 5. Output Files
nmap_output.txt — raw scan results

tcp_scan.pcap — (not included in repo)

## 6. Notes
All scans were performed in a controlled lab environment.
No external systems were targeted.
