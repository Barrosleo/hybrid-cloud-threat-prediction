# Model Card — Random Forest Threat Detection Model

## Overview
This model predicts whether a network flow is **Normal** or **Attack** using metadata features.

## Intended Use
- Network intrusion detection  
- Hybrid cloud threat monitoring  
- Security research and experimentation  

## Not Intended For
- Production SOC environments without further tuning  
- Encrypted traffic payload inspection  
- Zero-day attack detection  

## Performance
| Metric | Score |
|--------|-------|
| Accuracy | 0.9753 |
| Precision | 0.9767 |
| Recall | 0.9753 |
| F1 | 0.9760 |
| AU‑ROC | 0.6485 |

## Ethical Considerations
- Dataset is from 2012; modern traffic differs significantly  
- Encrypted protocols (TLS 1.3, QUIC) not represented  
- Risk of false positives in real-world environments  

## Limitations
- No adversarial robustness  
- Limited generalization to modern cloud workloads  
