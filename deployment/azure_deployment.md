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
