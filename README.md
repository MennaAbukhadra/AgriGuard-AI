# AgriGuard

AgriGuard is an end-to-end machine learning system for early crop stress detection using satellite imagery, climate data, and explainable AI.

The project predicts potential crop stress before visible symptoms appear, helping support proactive agricultural decision-making. It combines remote sensing data from Google Earth Engine, climate observations from NASA POWER, an XGBoost classification model, and an AI assistant that explains predictions in natural language. The system is delivered through an interactive Streamlit dashboard powered by a FastAPI backend. :contentReference[oaicite:0]{index=0}

---

## Overview

Traditional crop monitoring often detects problems only after damage has already occurred. AgriGuard addresses this challenge by continuously analyzing vegetation and climate indicators to estimate crop stress risk for each agricultural grid.

The study focuses on **Kafr El-Sheikh, Egypt**, where the agricultural area is divided into **1 km × 1 km grids**. For each grid, the system predicts the probability of crop stress and provides an explanation of the environmental factors that contributed to the prediction. :contentReference[oaicite:1]{index=1}

---

## Features

- Executive dashboard for monitoring key indicators
- Interactive crop stress risk map
- Grid-level inspection
- Crop stress prediction
- Model insights and feature importance
- AI assistant for explaining predictions
- REST API built with FastAPI
- Docker support for deployment

---

## System Architecture

```

Satellite Data (Google Earth Engine)
+
Climate Data (NASA POWER)
↓
Data Processing & Feature Engineering
↓
XGBoost Model
↓
FastAPI Backend
↓
Streamlit Dashboard
↓
Google Gemini AI Assistant

```

---

## Data Sources

The project combines multiple data sources:

- Sentinel-2 satellite imagery from Google Earth Engine
- NASA POWER climate data
- Vegetation indices including:
  - NDVI
  - NDWI
  - EVI
- Climate variables including:
  - Temperature
  - Rainfall
  - Relative Humidity
  - Wind Speed

The collected data covers agricultural grids in Kafr El-Sheikh from **2020 to 2024**. :contentReference[oaicite:2]{index=2}

---

## Feature Engineering

Several time-series and environmental features were engineered to improve predictive performance, including:

- Rolling statistics
- Lag features
- Seasonal encoding
- Cyclical date encoding
- Vegetation trends
- NDVI, NDWI, and EVI changes
- Vapor Pressure Deficit (VPD)
- Evapotranspiration (ET)
- Drought severity
- Temperature anomalies
- Composite agricultural risk score

Special care was taken to prevent data leakage by applying chronological processing and lag-based feature generation. :contentReference[oaicite:3]{index=3}

---

## Machine Learning

The final production model uses **XGBoost** for binary crop stress classification.

Model evaluation included:

- Logistic Regression
- Random Forest
- XGBoost

A time-based train/test split was used to preserve chronological order and simulate real deployment conditions. Hyperparameter optimization was performed using TimeSeriesSplit and RandomizedSearchCV. :contentReference[oaicite:4]{index=4}

### Performance

| Metric | Value |
|---------|-------|
| ROC-AUC | **0.957** |
| Precision | **0.53** |
| Recall | **0.75** |
| F1 Score | **0.62** |

---

## Explainable AI

Predictions are accompanied by natural language explanations generated using **Google Gemini**.

Instead of only displaying whether a grid is classified as healthy or stressed, the AI assistant explains the likely environmental causes behind the prediction, making the results easier to interpret for end users. :contentReference[oaicite:5]{index=5}

---

## Technologies Used

### Machine Learning

- Python
- Scikit-learn
- XGBoost
- Pandas
- NumPy

### Backend

- FastAPI
- Pydantic

### Frontend

- Streamlit
- Plotly

### AI

- Google Gemini API

### Deployment

- Docker
- Docker Compose

---

## Project Structure

```

AgriGuard
│
├── backend/
│   ├── services/
│   ├── saved_models/
│   ├── data/
│   ├── main.py
│   └── Dockerfile
│
├── frontend/
│   ├── pages/
│   ├── utils/
│   ├── app.py
│   └── Dockerfile
│
├── docs/
├── notebooks/
│
├── docker-compose.yml
└── README.md

```

---

## Running with Docker

Clone the repository:

```bash
git clone https://github.com/MennaAbukhadra/AgriGuard-AI.git

cd AgriGuard-AI
```

Build the project:

```bash
docker compose build
```

Run the application:

```bash
docker compose up
```

Once running:

Frontend:

```
http://localhost:8501
```

Backend:

```
http://localhost:8010/docs
```

---

## API Endpoints

| Endpoint | Description |
|-----------|-------------|
| `/dashboard` | Executive dashboard data |
| `/risk-map` | Risk map data |
| `/grid-inspection` | Grid inspection |
| `/predict` | Crop stress prediction |
| `/model-insights` | Model metrics and feature importance |
| `/chat` | AI assistant |

---

## Future Improvements

Possible future enhancements include:

- Real-time satellite updates
- Multi-crop support
- Additional governorates
- Historical trend analysis
- Mobile application
- Automated cloud deployment

---

## Acknowledgments

This project was developed as part of the **Digital Egypt Pioneers Initiative (DEPI)** and combines machine learning, remote sensing, climate analytics, and explainable AI to support precision agriculture.
