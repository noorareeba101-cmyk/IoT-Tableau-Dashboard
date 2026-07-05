IoT Smart Device Monitoring & Anomaly Detection Dashboard

An end-to-end IoT analytics project that simulates and analyzes industrial machine sensor data to detect equipment faults before they cause downtime. Built using Python for data processing and machine learning, and Tableau for interactive visualization.

Project Overview

Industrial equipment failures are costly and often preventable if warning signs are caught early. This project builds a monitoring system that:


Tracks key sensor metrics (temperature, vibration, acoustic signal, current) across multiple machines
Uses a machine learning model to automatically flag abnormal readings
Presents findings through an interactive Tableau dashboard for quick decision-making


Business Problem


Manufacturing plants rely on continuous machine uptime. Unexpected equipment failure leads to costly downtime and reactive maintenance. This project explores whether sensor data (vibration, temperature, acoustic, current) can be used to detect early warning signs of machine faults, enabling predictive maintenance instead of reactive repairs.



Dataset

Real-world industrial sensor dataset sourced from Kaggle: Predictive Maintenance Dataset, containing per-minute sensor readings from multiple machines, including:


timestamp, machine_id
vibration, acoustic, temperature, current
IMF_1, IMF_2, IMF_3 (signal decomposition features)
label (0 = Normal, 1 = Fault) — ground truth for model validation


Tools & Technologies


Python (pandas, scikit-learn) — data cleaning, feature engineering, anomaly detection
Tableau Desktop — interactive dashboard and visualization
TabPy — Python-Tableau integration for analytics extensions
Isolation Forest — unsupervised anomaly detection model


Workflow

1. Data Cleaning & Feature Engineering (clean_data.py)


Removed duplicates, checked for missing values
Engineered time-based features (hour, day, day of week)
Calculated rolling averages (5-minute window) for temperature, vibration, and current to smooth sensor noise


2. Anomaly Detection (anomaly_detection.py)


Trained an Isolation Forest model on sensor features to detect abnormal machine behavior
Validated predictions against the dataset's ground-truth fault labels


Model Performance:

MetricNormalFaultPrecision0.991.00Recall1.000.89F1-Score0.990.94

Overall Accuracy: 99%

The model correctly identified 180 of 202 actual faults with zero false alarms (100% precision on fault predictions) — meaning every alert raised was a genuine issue, which is critical for building trust in an automated monitoring system.

3. Interactive Dashboard (Tableau)

A 4-panel dashboard was built covering:


Total Machines — quick KPI overview
Temperature Trend Over Time — per-machine trend line to spot drift or spikes
Anomaly Detection (Temperature vs Vibration) — scatter plot clearly separating Normal vs Fault clusters
Fault Count by Machine — comparison of failure frequency across machines


Dashboard actions were added so selecting a machine filters all views to show that machine's data.

Key Insight

Machines exhibited a clear separation between normal and fault conditions in temperature-vibration space: fault readings clustered at both higher temperature and higher vibration than normal operation, suggesting these two metrics together are strong early indicators of impending failure and could drive a real-time alert threshold.


Author

Built as a hands-on portfolio project applying Python-based machine learning and Tableau visualization to an industrial IoT predictive maintenance use case.