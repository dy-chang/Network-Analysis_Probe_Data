# 🚧 Network Disruption Analysis Using INRIX ClearGuide Data  
### Case Study: Francis Scott Key Bridge Collapse (Baltimore, MD)

---

## 📍 Overview

This project analyzes the **network-wide traffic impacts** of the March 26, 2024 collapse of the Francis Scott Key Bridge using high-resolution INRIX ClearGuide data.

The objective is to move beyond simple before/after comparisons and provide:

- **Corridor-level impact identification**
- **Temporal persistence analysis**
- **Causal inference using statistical modeling**
- **Actionable insights for transportation planning and resilience**

---

## 🎯 Why This Project Matters

Infrastructure disruptions are rare but high-impact events.  
Understanding **where, when, and how impacts propagate** is critical for:

- Traffic operations
- Emergency response planning
- Long-term infrastructure resilience

This project demonstrates how large-scale traffic data can be transformed into **decision-ready insights**.

---

## 📊 Data

- Source: INRIX ClearGuide
- Temporal resolution: 15-minute intervals
- Spatial unit: Corridors (multi-link aggregated)
- Time span:
  - Pre-event: Feb 26 – Mar 25, 2024
  - Post-event: Mar 26 – Apr 25, 2024
  - Seasonal comparison: Fall 2023 vs Fall 2024, Winter 2023–24 vs 2024–25

---

## 🧠 Methodology

### 1. Baseline Comparison
- Before vs After analysis using:
  - Travel Time Index (TTI)
  - Average Speed
  - Delay

---

### 2. Stratified Analysis
- Focus on **Top 20% most impacted corridors**
- Reveals heterogeneity masked by aggregate statistics

---

### 3. Seasonal Robustness
- Compares:
  - Immediate impact
  - Fall recovery
  - Winter persistence
- Identifies whether disruption effects are temporary or structural

---

### 4. Causal Modeling

#### Fixed Effects Model
Controls for:
- Corridor-specific characteristics
- Time-invariant heterogeneity

#### Difference-in-Differences (DiD)
- Treatment: Mid-Far corridors  
- Control: Far corridors  
- Measures **causal impact of network disruption**

#### Mixed Effects Model
- Captures both fixed and random variations across corridors

---

## 🔍 Key Findings

- Significant increases in congestion across multiple corridors
- Impacts were **spatially uneven**, concentrated in specific routes
- 일부 corridors는 Fall/Winter까지 영향 지속 (persistent disruption)
- 단순 평균 분석으로는 **critical corridors 식별 불가능**

---

## 🧩 Technical Highlights

- Large-scale time-series data processing (15-min resolution)
- Panel data modeling (Fixed Effects, Mixed Models)
- Causal inference (Difference-in-Differences)
- Transportation domain integration (TTI, delay, corridor analysis)

---

## 🗂 Project Structure





```text
clearguide-bridge-impact-portfolio/
├── notebooks/
│   └── 01_clearguide_bridge_impact_portfolio.ipynb
├── src/
│   └── analysis_utils.py
├── data/
│   └── (not included – user-provided ClearGuide dataset)
├── figures/
│   └── (recommended: key result plots)
├── archive/
│   └── original_notebooks/
└── README.md

---

## 🚀 How to Run

1. Clone the repository
2. Add dataset:
3. Install dependencies:
4. Run notebook:



