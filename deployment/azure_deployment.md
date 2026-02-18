# Azure ML Deployment Guide

This document explains how to deploy the trained Random Forest model as an Azure ML endpoint.

---

## 1. Create Azure ML Workspace

```bash
az ml workspace create \
  --name hybrid-ml-ws \
  --resource-group hybrid-ml-rg \
  --location uksouth
```
## 2. Register the Model
Upload your model:

```bash
az ml model create \
  --name rf-threat-model \
  --path models/random_forest.pkl \
  --type custom_model
```

## 3. Create an Environment
```bash
az ml environment create \
  --name rf-env \
  --image mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04 \
  --conda-file environment.yml
```

## 4. Create an Inference Endpoint
```bash
az ml online-endpoint create \
  --name threat-detection-endpoint \
  --auth-mode key
```

## 5. Deploy the Model
```bash
az ml online-deployment create \
  --name blue \
  --endpoint-name threat-detection-endpoint \
  --model rf-threat-model:1 \
  --environment rf-env:1 \
  --code src/ \
  --entry-script score.py \
  --instance-type Standard_DS2_v2 \
  --instance-count 1
```

## 6. Test the Endpoint
```bash
az ml online-endpoint invoke \
  --name threat-detection-endpoint \
  --request-file sample_request.json
```

## 7. Example JSON Payload
```json
{
  "Dur": 0.12,
  "Proto_encoded": 1,
  "SrcPort": 443,
  "DstPort": 51514,
  "Packets": 10,
  "Bytes": 850
}
```

## 8. Monitor Logs
```bash
az ml online-deployment get-logs \
  --name blue \
  --endpoint-name threat-detection-endpoint
```

## 9. Scale the Endpoint
```bash
az ml online-deployment update \
  --name blue \
  --endpoint-name threat-detection-endpoint \
  --instance-count 3
```
