# TCP Port Scan Simulation

This folder documents the TCP SYN scan simulation.

## Steps Performed
1. Used Nmap to generate SYN scan traffic.
2. Captured flows using tcpdump/Wireshark.
3. Extracted metadata for ML model.
4. Sent JSON payload to Azure ML endpoint.
5. Verified correct classification.

## Example Command
```
nmap -sS 10.0.0.5
```
