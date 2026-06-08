<div align="center">

# Network Intrusion Detection System

### End-to-End Machine Learning & MLOps Pipeline for Cyber Threat Detection

<br/>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![MLflow](https://img.shields.io/badge/MLflow-2.0+-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)](https://mlflow.org)
[![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![AWS](https://img.shields.io/badge/AWS_S3_|_ECR-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![DagsHub](https://img.shields.io/badge/DagsHub-FF6B35?style=for-the-badge&logo=dagshub&logoColor=white)](https://dagshub.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br/>

> *A fully automated machine learning system engineered to detect and classify malicious network traffic at scale — built with the rigor of production software engineering and the precision of modern MLOps.*

<br/>

[Overview](#project-overview) &nbsp;•&nbsp; [Architecture](#system-architecture) &nbsp;•&nbsp; [Pipeline](#end-to-end-pipeline-workflow) &nbsp;•&nbsp; [Components](#pipeline-components) &nbsp;•&nbsp; [API](#fastapi-rest-api) &nbsp;•&nbsp; [Deployment](#deployment) &nbsp;•&nbsp; [Setup](#getting-started)

</div>

---

## Project Overview

The **Network Intrusion Detection System** is an end-to-end Machine Learning and MLOps solution engineered to identify malicious network activities and cyber threats using advanced supervised learning techniques.

This system goes far beyond conventional notebook-based prototypes. Every stage of the machine learning lifecycle — from raw data ingestion to cloud deployment — is architected as an **independent, modular, and reusable component**, following the highest standards of software engineering and MLOps maturity.

At its core, the system:

- **Ingests** raw network traffic data from MongoDB Atlas
- **Validates** data quality and detects statistical drift using the Kolmogorov-Smirnov test
- **Transforms** features through an automated preprocessing pipeline with KNN imputation
- **Trains** five candidate classification models with automated hyperparameter optimization
- **Tracks** every experiment automatically via MLflow and DagsHub
- **Deploys** a production inference service through a containerized FastAPI application
- **Automates** the entire build, test, and deployment lifecycle through a GitHub Actions CI/CD pipeline

The result is a **reproducible, scalable, and observable** system ready for real-world production environments.

---

## Problem Statement

Modern organizations generate billions of network events daily. Manual monitoring is operationally infeasible, and rule-based detection systems fail to adapt to evolving threat landscapes. Traditional approaches are brittle, slow to update, and unable to generalize across diverse attack patterns.

This project addresses that gap by delivering an **automated, data-driven classification system** capable of analyzing network-level features and distinguishing legitimate traffic from malicious intrusions — at scale, with measurable accuracy, and with full reproducibility.

The solution is not a one-time experiment. It is a **living, deployable system** with automated retraining infrastructure, cloud artifact versioning, and a REST API — designed to evolve alongside the threat environment it monitors.

---

## Feature Highlights

| Category | Feature | Description |
|:---|:---|:---|
| **Architecture** | Modular Pipeline Design | Each stage is a fully decoupled, independently testable component |
| **Data** | MongoDB Atlas Integration | Scalable NoSQL storage with automated ingestion workflows |
| **Quality** | Automated Data Validation | Schema enforcement, integrity checks, and feature compatibility verification |
| **Reliability** | Statistical Drift Detection | Kolmogorov-Smirnov test applied per feature on every run |
| **Preprocessing** | KNN-Based Imputation | Relationship-preserving missing value handling |
| **Modeling** | Multi-Model Evaluation | Five classifiers trained with automated best-model selection |
| **Optimization** | GridSearchCV Tuning | Exhaustive hyperparameter search across all candidate models |
| **Observability** | MLflow Experiment Tracking | Full logging of metrics, parameters, and model artifacts per run |
| **Registry** | DagsHub Integration | Centralized, versioned remote model registry |
| **Cloud** | AWS S3 Artifact Management | Automated cloud sync of all pipeline artifacts and model binaries |
| **Inference** | FastAPI REST Service | Production-grade prediction API with Swagger documentation |
| **Portability** | Docker Containerization | Consistent, environment-agnostic deployments |
| **Automation** | GitHub Actions CI/CD | Fully automated integration, delivery, and deployment pipeline |
| **Container Registry** | AWS ECR | Managed container image versioning and storage |

---

## Technology Stack

<table>
<tr>
<td valign="top" width="50%">

**Core**
| Layer | Technology |
|:---|:---|
| Language | Python 3.8+ |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Statistical Testing | SciPy |

**Storage & Database**
| Layer | Technology |
|:---|:---|
| Primary Database | MongoDB Atlas |
| Artifact Storage | AWS S3 |
| Container Registry | AWS ECR |

</td>
<td valign="top" width="50%">

**MLOps & Observability**
| Layer | Technology |
|:---|:---|
| Experiment Tracking | MLflow |
| Model Registry | DagsHub |

**Infrastructure**
| Layer | Technology |
|:---|:---|
| API Framework | FastAPI |
| Containerization | Docker |
| CI/CD | GitHub Actions |

</td>
</tr>
</table>

---

## System Architecture

```
+------------------------------------------------------------------+
|                         DATA LAYER                               |
|                                                                  |
|               Raw Network Dataset (CSV)                          |
|                          |                                       |
|                          v                                       |
|                MongoDB Atlas Collection                          |
+------------------------------+-----------------------------------+
                               |
                               v
+------------------------------------------------------------------+
|                        ML PIPELINE                               |
|                                                                  |
|   +---------------+   +---------------+   +------------------+  |
|   |     Data      |   |     Data      |   |      Data        |  |
|   |   Ingestion   +-->+   Validation  +-->+  Transformation  |  |
|   |               |   |  + KS Drift   |   |  + KNN Imputer   |  |
|   +---------------+   +---------------+   +--------+---------+  |
|                                                    |             |
|                                                    v             |
|                                          +-----------------+    |
|                                          |  Model Training |    |
|                                          |  GridSearchCV   |    |
|                                          |  5 Classifiers  |    |
|                                          +--------+--------+    |
+---------------------------------------------------+-------------+
                                                    |
                          +-------------------------+
                          |                         |
                          v                         v
              +--------------------+   +------------------------+
              |       MLflow       |   |         DagsHub        |
              |  Experiment Logs   |   |     Model Registry     |
              |  Metrics & Params  |   |   Versioned Artifacts  |
              +--------------------+   +------------------------+
                          |
                          v
              +--------------------+
              |       AWS S3       |
              |  Artifact Storage  |
              |  model.pkl         |
              |  preprocessor.pkl  |
              +---------+----------+
                        |
                        v
+------------------------------------------------------------------+
|                      SERVING LAYER                               |
|                                                                  |
|               FastAPI Application (Docker)                       |
|                          |                                       |
|             +------------+-----------+                          |
|             v                        v                          |
|       GET /train               POST /predict                    |
|   (Trigger Pipeline)        (Batch Inference)                   |
+------------------------------------------------------------------+
```

---

## Repository Structure

```
networksecurity/
|
+-- app.py                          # FastAPI application — prediction & training endpoints
+-- main.py                         # Pipeline orchestration entry point
+-- push_data.py                    # MongoDB data ingestion utility
+-- Dockerfile                      # Container build specification
+-- requirements.txt                # Python dependency manifest
+-- setup.py                        # Package configuration
+-- .env                            # Environment variable definitions (not committed)
|
+-- .github/
|   +-- workflows/
|       +-- main.yml                # GitHub Actions — CI/CD workflow definition
|
+-- Network_Data/
|   +-- phisingData.csv             # Source network traffic dataset
|
+-- data_schema/
|   +-- schema.yaml                 # Feature schema and validation rules
|
+-- templates/
|   +-- table.html                  # Prediction results HTML rendering template
|
+-- final_model/
|   +-- model.pkl                   # Serialized production model artifact
|   +-- preprocessor.pkl            # Serialized preprocessing pipeline artifact
|
+-- prediction_output/              # Batch prediction result storage
+-- Artifacts/                      # Auto-generated pipeline stage artifacts
|
+-- networksecurity/                # Core package
    |
    +-- components/                 # Pipeline stage implementations
    |   +-- data_ingestion.py       # Stage 1 — MongoDB extraction & splitting
    |   +-- data_validation.py      # Stage 2 — Schema & drift validation
    |   +-- data_transformation.py  # Stage 3 — Feature engineering & imputation
    |   +-- model_trainer.py        # Stage 4 — Training, tuning & selection
    |
    +-- pipeline/
    |   +-- training_pipeline.py    # Orchestrates all 4 training stages
    |   +-- batch_prediction.py     # Batch inference pipeline
    |
    +-- cloud/
    |   +-- s3_syncer.py            # AWS S3 artifact synchronization
    |
    +-- entity/
    |   +-- artifact_entity.py      # Artifact dataclass definitions
    |   +-- config_entity.py        # Configuration dataclass definitions
    |
    +-- constant/
    |   +-- training_pipeline/      # Pipeline-wide constants
    |
    +-- logging/                    # Structured logging module
    +-- exception/                  # Custom exception handling with traceback enrichment
    |
    +-- utils/
        +-- main_utils/             # General-purpose utilities (serialization, I/O)
        +-- ml_utils/               # ML utilities (metrics, model evaluation, estimators)
```

---

## End-to-End Pipeline Workflow

```
  +-------------------------------------------------------------------------+
  |                                                                         |
  |  MongoDB Atlas — Raw network traffic records                            |
  |         |                                                               |
  |         v                                                               |
  |  +--------------------------------------------------------------+      |
  |  |  STAGE 1 — Data Ingestion                                    |      |
  |  |  - Connect to MongoDB, extract NetworkData collection        |      |
  |  |  - Clean _id fields, standardize null representations        |      |
  |  |  - Persist to feature store for lineage tracking             |      |
  |  |  - 80/20 stratified train-test split                         |      |
  |  +------------------------------+-------------------------------+      |
  |                                 |  train.csv  |  test.csv              |
  |                                 v                                       |
  |  +--------------------------------------------------------------+      |
  |  |  STAGE 2 — Data Validation                                   |      |
  |  |  - Enforce schema rules from schema.yaml                     |      |
  |  |  - Verify column count and feature compatibility             |      |
  |  |  - KS Test per feature  -->  drift_report.yaml              |      |
  |  +------------------------------+-------------------------------+      |
  |                                 |  valid_train.csv  |  valid_test      |
  |                                 v                                       |
  |  +--------------------------------------------------------------+      |
  |  |  STAGE 3 — Data Transformation                               |      |
  |  |  - Separate features from target column (Result)             |      |
  |  |  - Remap labels: -1 --> 0 for binary classification         |      |
  |  |  - KNNImputer(n_neighbors=3) for missing values             |      |
  |  |  - Serialize preprocessor --> preprocessing.pkl             |      |
  |  +------------------------------+-------------------------------+      |
  |                                 |  train.npy  |  test.npy              |
  |                                 v                                       |
  |  +--------------------------------------------------------------+      |
  |  |  STAGE 4 — Model Training                                    |      |
  |  |  - Train 5 classifiers with GridSearchCV                     |      |
  |  |  - Evaluate on F1 Score, Precision, Recall                   |      |
  |  |  - Select best model automatically                           |      |
  |  |  - Log all experiments to MLflow  -->  DagsHub              |      |
  |  |  - Bundle model + preprocessor  -->  NetworkModel           |      |
  |  |  - Serialize to model.pkl + final_model/                    |      |
  |  +------------------------------+-------------------------------+      |
  |                                 |                                       |
  |                                 v                                       |
  |  AWS S3 Sync — All artifacts and models pushed to cloud                |
  |                                 |                                       |
  |                                 v                                       |
  |  FastAPI — Inference service live at /predict                          |
  |                                                                         |
  +-------------------------------------------------------------------------+
```

---

## Pipeline Components

### Stage 1 — Data Ingestion

Establishes a secure connection to MongoDB Atlas and extracts raw network traffic records from the `NetworkData` collection within the `NETWORK_DATABASE` database. Records are converted into a structured Pandas DataFrame, cleaned of MongoDB internals (`_id` fields), and standardized by replacing string-encoded null markers (`"na"`) with proper `NaN` values. The cleaned dataset is persisted to a local feature store to preserve data lineage, then partitioned into training and testing sets using an 80/20 split.

**Artifact Output:**
```
Artifacts/Data_Ingestion/
+-- feature_store/
|   +-- phisingData.csv       <- Raw cleaned dataset
+-- ingested/
    +-- train.csv             <- 80% training partition
    +-- test.csv              <- 20% evaluation partition
```

---

### Stage 2 — Data Validation

Enforces strict data quality contracts before any feature engineering occurs. Every incoming dataset is validated against the schema defined in `data_schema/schema.yaml`, verifying column count, feature names, data types, and structural integrity.

Statistical drift detection is performed using the **Kolmogorov-Smirnov (KS) Test** — a non-parametric test that compares the empirical distributions of each feature between the training and test sets. A `drift_status: True` flag triggers a warning in the pipeline log, enabling proactive detection of distributional shift before model training.

```yaml
# Sample drift report — drift_report.yaml
feature_name:
  p_value: 0.87
  drift_status: False
```

**Artifact Output:**
```
Artifacts/Data_Validation/
+-- valid_train.csv
+-- valid_test.csv
+-- drift_report.yaml
```

---

### Stage 3 — Data Transformation

Converts validated raw datasets into numerical arrays ready for model ingestion. The transformation pipeline separates the target column (`Result`) from input features, remaps class labels from `{-1, 1}` to `{0, 1}` to conform to standard binary classification conventions, and applies KNN Imputation to handle missing values in a relationship-aware manner.

```python
KNNImputer(n_neighbors=3, weights="uniform")
```

The fitted preprocessor object is serialized and stored separately, ensuring that identical transformations can be applied deterministically during inference without recomputation.

**Artifact Output:**
```
Artifacts/Data_Transformation/
+-- train.npy              <- Transformed training array
+-- test.npy               <- Transformed evaluation array
+-- preprocessing.pkl      <- Serialized preprocessing pipeline
```

---

### Stage 4 — Model Training

The core modeling stage evaluates five classification algorithms, performs exhaustive hyperparameter optimization via GridSearchCV, and selects the highest-performing model based on evaluation metrics. All experiments are automatically tracked and logged to MLflow and DagsHub.

**Candidate Models and Hyperparameter Search Space:**

| Model | Hyperparameter | Search Values |
|:---|:---|:---|
| Random Forest | `n_estimators` | 8, 16, 32, 128, 256 |
| Decision Tree | `criterion` | gini, entropy, log_loss |
| Gradient Boosting | `learning_rate` | 0.001, 0.01, 0.05, 0.1 |
| | `subsample` | 0.6, 0.7, 0.75, 0.85, 0.9 |
| | `n_estimators` | 8, 16, 32, 64, 128, 256 |
| Logistic Regression | — | Baseline (no tuning) |
| AdaBoost | `learning_rate` | 0.001, 0.01, 0.1 |
| | `n_estimators` | 8, 16, 32, 64, 128, 256 |

**Evaluation Metrics:**

| Metric | Purpose |
|:---|:---|
| F1 Score | Harmonic mean of precision and recall — primary selection criterion |
| Precision | Fraction of predicted intrusions that are actual intrusions |
| Recall | Fraction of actual intrusions correctly identified |

The best-performing model is bundled together with the preprocessor into a unified `NetworkModel` object, serialized, and saved both to the pipeline artifact directory and to `final_model/` for deployment.

---

## Experiment Tracking — MLflow & DagsHub

Every training run is fully instrumented. MLflow logs hyperparameters, evaluation metrics, and model artifacts for both training and test evaluations. DagsHub serves as the centralized remote tracking server and model registry, providing a persistent, collaborative experiment history accessible from any environment.

```
MLflow Run (per training execution)
+-- Metrics
|   +-- f1_score         (train + test)
|   +-- precision        (train + test)
|   +-- recall_score     (train + test)
+-- Model Artifact       (sklearn model binary)
+-- Registry Entry       -> networksecurity_model (versioned)
```

**DagsHub Repository:** `johankar555/network_intrusion_detection_system`

---

## AWS Cloud Integration

### S3 Artifact Storage

The training pipeline automatically synchronizes all generated artifacts to AWS S3 upon completion, enabling centralized versioning, backup, and cross-environment access.

| Asset | S3 Path |
|:---|:---|
| Pipeline stage artifacts | `s3://<bucket>/Artifacts/` |
| Production model binary | `s3://<bucket>/final_model/model.pkl` |
| Preprocessing pipeline | `s3://<bucket>/final_model/preprocessor.pkl` |

### ECR Container Registry

Docker images are built and pushed to **AWS Elastic Container Registry (ECR)** as part of the CI/CD pipeline, ensuring immutable, versioned container images are available for production deployment.

---

## FastAPI REST API

The system exposes a clean, documented REST API for both triggering pipeline runs and serving predictions.

### Endpoints

| Method | Endpoint | Description |
|:---:|:---|:---|
| `GET` | `/` | Redirects to interactive Swagger UI documentation |
| `GET` | `/train` | Triggers the full end-to-end training pipeline |
| `POST` | `/predict` | Accepts a CSV upload and returns batch predictions |

### Prediction Request Flow

```
POST /predict  (multipart/form-data — CSV file)
       |
       v
Load preprocessor.pkl  ->  Load model.pkl
       |
       v
Transform input features using fitted preprocessor
       |
       v
Generate class predictions via trained model
       |
       v
Append predictions column to input DataFrame
       |
       v
Save results -> prediction_output/output.csv
       |
       v
Return rendered HTML table (templates/table.html)
```

**Interactive API Documentation:** `http://localhost:8000/docs`

---

## CI/CD Pipeline — GitHub Actions

A fully automated three-phase pipeline is triggered on every push to the `main` branch.

### Phase 1 — Continuous Integration

| Step | Action |
|:---|:---|
| Repository Checkout | Clone latest source |
| Dependency Installation | `pip install -r requirements.txt` |
| Code Linting | Enforce code quality standards |
| Unit Testing | Validate component behavior |
| Build Validation | Confirm package integrity |

### Phase 2 — Continuous Delivery

| Step | Action |
|:---|:---|
| AWS Credential Configuration | Authenticate with IAM |
| ECR Authentication | `aws ecr get-login-password` |
| Docker Image Build | `docker build -t networksecurity .` |
| Image Push to ECR | Tagged, versioned container push |

### Phase 3 — Continuous Deployment (Self-Hosted Runner)

```
Push to main
      |
      v
GitHub Actions Triggered
      |
      v
Docker Image Built & Pushed to AWS ECR
      |
      v
Self-Hosted Runner: Pull Latest Image from ECR
      |
      v
Stop & Remove Existing Container
      |
      v
Launch New Container  ->  Service Live on Port 8000
```

---

## Deployment

### Docker

**Build the image:**
```bash
docker build -t networksecurity .
```

**Run the container:**
```bash
docker run -p 8000:8000 \
  --env-file .env \
  networksecurity
```

**Access the API:**
```
http://localhost:8000/docs
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Docker
- AWS CLI configured with appropriate IAM permissions
- MongoDB Atlas cluster
- DagsHub account with MLflow tracking enabled

### 1. Clone the Repository

```bash
git clone https://github.com/johankar555/network_intrusion_detection_system.git
cd network_intrusion_detection_system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
MONGO_DB_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=your_aws_region
DAGSHUB_TOKEN=your_dagshub_personal_access_token
```

### 4. Push Data to MongoDB (First Run Only)

```bash
python push_data.py
```

### 5. Run the Training Pipeline

```bash
python main.py
```

### 6. Start the Prediction Service

```bash
python app.py
```

**API available at:** `http://localhost:8000`  
**Swagger docs at:** `http://localhost:8000/docs`

---

## Project Highlights

| Capability | Detail |
|:---|:---|
| Modular MLOps Architecture | Every pipeline stage is independently testable and reusable |
| Automated Model Selection | Best model chosen programmatically — no manual intervention required |
| Statistical Drift Detection | KS Test applied per feature on every pipeline execution |
| Full Experiment Lineage | Every run is traceable via MLflow and DagsHub |
| Cloud-Native Artifact Management | All outputs versioned and stored in AWS S3 |
| Production-Ready API | FastAPI with auto-generated OpenAPI documentation |
| Containerized Deployment | Docker ensures environment parity from development to production |
| Fully Automated CI/CD | Code push to deployment requires zero manual steps |
| Reproducible Workflows | Identical results guaranteed across any execution environment |

---

## Roadmap

- [ ] **Real-Time Streaming Inference** — Kafka-based event-driven prediction pipeline
- [ ] **Model Monitoring Dashboard** — Drift alerting and performance degradation detection
- [ ] **Automated Retraining Triggers** — Scheduled and drift-triggered retraining workflows
- [ ] **Kubernetes Orchestration** — Horizontal scaling via Helm chart deployment
- [ ] **Dedicated Feature Store** — Feast or Tecton integration for feature governance
- [ ] **Data Quality Framework** — Great Expectations integration for assertion-based validation
- [ ] **Advanced Threat Analytics** — SHAP-based explainability for detected intrusions
- [ ] **Automated Incident Response** — PagerDuty / OpsGenie alerting on anomaly detection

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with precision. Deployed with confidence. Monitored with intent.**

*If this project was useful or informative, consider giving it a star — it helps others discover it.*

</div>