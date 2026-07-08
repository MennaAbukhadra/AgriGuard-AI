# AgriGuard AI

An end-to-end crop stress prediction platform that combines satellite imagery, climate observations, machine learning, and explainable AI to predict crop stress up to **15 days before visible symptoms appear**.

---

## Overview

AgriGuard is an intelligent crop monitoring system designed to support early agricultural decision-making through predictive analytics. The platform combines Sentinel-2 satellite imagery, NASA POWER climate observations, feature engineering, and an XGBoost model to estimate crop stress before visible symptoms appear.

The system includes a FastAPI backend, an interactive Streamlit dashboard, and an AI assistant that provides natural-language explanations for model predictions. The application is fully containerized using Docker and prepared for deployment on Microsoft Azure.

---

## Project Highlights

| Item | Value |
|------|-------|
| Forecast Window | 15 Days |
| Study Area | Kafr El-Sheikh, Egypt |
| Observation Period | 2020–2024 |
| Spatial Resolution | 1 km × 1 km |
| Agricultural Grids | 2,828 |
| Machine Learning Model | XGBoost |
| Backend | FastAPI |
| Frontend | Streamlit |
| Deployment | Docker & Azure |

---

## Features

| Feature | Description |
|---------|-------------|
| Crop Stress Prediction | Predict crop stress up to 15 days in advance |
| Executive Dashboard | Visualize crop health and key performance indicators |
| Risk Map | Explore crop stress across agricultural grids |
| Grid Inspection | Analyze environmental variables for individual grids |
| AI Assistant | Generate natural-language explanations for predictions |
| REST API | Serve predictions through FastAPI |
| Docker Support | Run the complete application using containers |
| Azure Ready | Prepared for cloud deployment |

---

## System Architecture

```text
 Sentinel-2 Imagery          NASA POWER API
          │                        │
          └────────────┬───────────┘
                       │
               Data Collection
                       │
               Data Preprocessing
                       │
              Feature Engineering
                       │
                  XGBoost Model
                       │
                 FastAPI Backend
                ┌────────┴────────┐
                │                 │
         Streamlit Dashboard   AI Assistant
                │
                ▼
              End User
```

---

## Project Workflow

```text
Satellite Data
       +
Climate Data
       │
       ▼
Data Collection
       │
       ▼
Preprocessing
       │
       ▼
Feature Engineering
       │
       ▼
Model Training
       │
       ▼
Prediction API
       │
       ▼
Dashboard & AI Assistant
```

---

## Dataset

The model was trained using satellite imagery and climate observations collected for agricultural areas in **Kafr El-Sheikh, Egypt**.

| Property | Value |
|----------|------:|
| Observation Period | 2020–2024 |
| Agricultural Grids | 2,828 |
| Spatial Resolution | 1 km × 1 km |
| Observations | 330K+ |
| Engineered Features | 100+ |

### Data Sources

**Satellite Data**
- Sentinel-2
- NDVI
- NDWI
- EVI

**Climate Data**
- Temperature
- Rainfall
- Relative Humidity
- Wind Speed
- Solar Radiation

---

## Feature Engineering

Feature engineering is a core component of the project. Instead of relying only on raw environmental variables, the dataset was enriched with temporal and domain-specific features to improve predictive performance.

Generated features include:

- Rolling statistics
- Lag features
- Percentage change
- Vegetation anomalies
- Temperature anomalies
- Rainfall accumulation
- Vapor Pressure Deficit (VPD)
- Evapotranspiration (ET)
- Drought severity
- Seasonal encoding
- Cyclical time encoding

All temporal features were generated chronologically for each agricultural grid to prevent data leakage and simulate real-world prediction scenarios.

---

## Machine Learning

Several machine learning algorithms were evaluated during development. **XGBoost** was selected as the final production model because it achieved the best balance between predictive performance, inference speed, and robustness on structured agricultural data.

### Training Pipeline

- Time-based train/test split
- RandomizedSearchCV
- TimeSeries Cross Validation
- Threshold optimization
- Explainability integration

### Performance

| Metric | Value |
|---------|------:|
| Model | XGBoost |
| AUC-ROC | **0.957** |
| Decision Threshold | **0.80** |
| Validation Strategy | Time-Based Split |

---

## Explainable AI

To improve model transparency, each prediction is accompanied by a natural-language explanation generated using Google Gemini.

The explanation summarizes:

- Predicted crop condition
- Stress probability
- Environmental factors influencing the prediction
- Recommended actions

This enables users to understand **why** a prediction was generated instead of relying only on probability scores.

---

## Dashboard

The Streamlit dashboard provides multiple interactive views for monitoring crop conditions and exploring model predictions.

Modules include:

- Executive Dashboard
- Risk Map
- Grid Inspection
- Crop Stress Prediction
- Model Insights
- AI Assistant

---

## Dockerization

The project was fully containerized using Docker to simplify deployment and ensure consistent execution across different environments.

Key improvements include:

- Separation of Backend and Frontend services
- Dedicated Dockerfiles
- Docker Compose orchestration
- Dynamic file paths using `pathlib`
- Environment variables for API configuration
- Internal Docker networking

Run the complete application using:

```bash
docker compose build
docker compose up
```

---

## Azure Deployment

The application was prepared for deployment using **Microsoft Azure Container Apps**.

Deployment workflow:

1. Verify local execution.
2. Build Docker images.
3. Configure environment variables.
4. Deploy Backend and Frontend containers.
5. Validate communication between services.

---

## Project Structure

```text
AgriGuard-AI/
│
├── backend/
├── frontend/
├── data/
├── notebooks/
├── saved_models/
├── assets/
├── docker-compose.yml
└── README.md
```

---

## Installation

```bash
git clone <repository-url>

cd AgriGuard-AI

python -m venv .venv

pip install -r requirements.txt

uvicorn backend.main:app --reload --port 8010

streamlit run frontend/app.py
```

Or run using Docker:

```bash
docker compose build
docker compose up
```

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Machine Learning | XGBoost, Scikit-learn |
| Data Processing | Pandas, NumPy |
| Backend | FastAPI |
| Frontend | Streamlit |
| Visualization | Plotly, Folium |
| Remote Sensing | Google Earth Engine |
| Climate Data | NASA POWER API |
| Explainability | Google Gemini |
| Deployment | Docker, Microsoft Azure |
| Version Control | Git, GitHub |

---

## Acknowledgements

This project was developed as part of the **Digital Egypt Pioneers Initiative (DEPI)**.

We would like to acknowledge the open-source tools and platforms that supported this work, including Google Earth Engine, NASA POWER API, FastAPI, Streamlit, XGBoost, Docker, Microsoft Azure, and Google Gemini.

---

## License

This project was developed for educational and research purposes.
