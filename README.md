# Hybrid Cloud Threat Prediction (Machine Learning)

This project implements a machine-learning–based threat prediction system for hybrid cloud environments.  
It is based on my BSc Cyber Security dissertation at the University of West London.

## 🚀 Project Overview
Hybrid cloud environments introduce complex security challenges.  
This project uses machine learning to analyse network traffic and predict cyber threats before they occur.

The system:
- Processes real network traffic (ISCX IDS 2012 dataset)
- Performs feature engineering, normalization, and encoding
- Trains multiple ML models (Random Forest, SVM, Gradient Boosting)
- Achieves **97.53% accuracy** using Random Forest
- Simulates real attacks (NTP amplification, TCP port scan)
- Deploys the model in a hybrid cloud architecture using Azure ML Studio

## 🧠 Machine Learning Models
| Model | Test Accuracy | Precision | Recall | F1-Score |
|-------|---------------|-----------|--------|----------|
| Random Forest | 0.9753 | 0.9767 | 0.9753 | 0.9760 |
| Gradient Boosting | 0.9560 | 0.9653 | 0.9560 | 0.9606 |
| SVM | 0.8407 | 0.8407 | 0.8407 | 0.8407 |

## 🏗 Architecture
- Hybrid cloud environment (on-prem + Azure)
- Azure ML Studio for model deployment
- Python-based preprocessing and training pipeline
- Attack simulation environment for real-time testing

## 📂 Repository Structure
(Insert the folder tree here)

## 🔧 Technologies Used
- Python, Pandas, NumPy, Scikit-learn
- Azure ML Studio
- Google Colab Pro+
- Linux, Wireshark, pcap tools

## 📈 Results
- 97.53% accuracy
- Successful detection of NTP amplification and TCP port scanning
- Robust performance across multiple metrics

## 📜 Dissertation
This project is based on my final-year dissertation:
**“Predictive Analytics of Cyber Threats in Hybrid Cloud Environments: A Machine Learning Approach.”**
