### Network Security Projects For Phising Data

Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = 788614365622.dkr.ecr.us-east-1.amazonaws.com/networkssecurity
ECR_REPOSITORY_NAME = networkssecurity


Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker





# 🛡️ Network Security – Phishing Website Detection ML Pipeline

An end-to-end, production-ready Machine Learning pipeline for detecting phishing websites.  
This project demonstrates clean ML engineering practices including modular pipelines, artifact tracking, data validation, model training, batch prediction, Docker support, and CI integration.

---

## 📌 Project Overview

This system builds a complete ML workflow for phishing detection:

- Data Ingestion
- Data Validation (Schema + Drift Detection)
- Data Transformation
- Model Training & Evaluation
- Artifact Management
- Batch Prediction
- Cloud Sync Support
- Dockerization
- CI Workflow Integration

The architecture focuses on **scalability, reproducibility, and clean software engineering design**.

---

## 🎯 Problem Statement

Phishing websites mimic legitimate websites to steal user information.

This project trains a classification model to predict whether a website is:

- ✅ Legitimate  
- ❌ Phishing  

---

## 🏗️ Project Architecture

The system follows a modular ML pipeline architecture:
networksecurity/
│
├── components/ # ML pipeline components
├── pipeline/ # Training & prediction pipelines
├── entity/ # Config & artifact entities
├── constant/ # Project-wide constants
├── utils/ # Utility functions
├── logging/ # Custom logging module
├── exception/ # Custom exception handling
├── cloud/ # S3 sync utilities


---

## 🔄 ML Pipeline Flow

1. Data Ingestion  
2. Data Validation  
   - Schema validation  
   - Data drift detection  
3. Data Transformation  
   - Preprocessing  
   - Train/Test split  
4. Model Training  
5. Model Evaluation  
6. Model Saving  
7. Batch Prediction  

All outputs are stored inside timestamped `Artifacts/` directories for reproducibility.

---

## 📂 Complete Project Structure
networksecurity/
│
├── app.py
├── main.py
├── push_data.py
├── Dockerfile
├── requirements.txt
├── setup.py
│
├── data_schema/
│ └── schema.yaml
│
├── final_model/
│ ├── model.pkl
│ └── preprocessor.pkl
│
├── Artifacts/
├── logs/
├── Network_Data/
├── prediction_output/
├── templates/

---

## ⚙️ Core Components Explained

### 1️⃣ Data Ingestion
- Reads phishing dataset
- Splits data into train/test
- Saves ingestion artifacts

### 2️⃣ Data Validation
- Validates schema using `schema.yaml`
- Detects data drift
- Generates validation report

### 3️⃣ Data Transformation
- Applies preprocessing pipeline
- Saves `preprocessor.pkl`
- Outputs transformed `.npy` datasets

### 4️⃣ Model Trainer
- Trains classification model
- Evaluates metrics
- Saves:
  - `model.pkl`
  - `preprocessor.pkl`

### 5️⃣ Batch Prediction
- Loads trained model
- Performs inference on new data
- Saves predictions to:
prediction_output/output.csv

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd networksecurity
## Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate        # Windows

## Install dependencies
pip install -r requirements.txt

## Run the application
python app.py



