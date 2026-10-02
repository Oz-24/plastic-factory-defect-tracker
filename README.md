# Sustainable Plastic Manufacturing Performance Analyzer

A lightweight, high-performance industrial data cleaning and efficiency tracking script built using Python, Pandas, and NumPy. This repository serves as a portfolio demonstration of foundational data engineering.

## 🏭 Project Overview
In industrial manufacturing, minimizing material scrap rates is critical for both bottom-line financial profitability and environmental sustainability. This project simulates real-time production telemetry from a plastic injection-molding facility. It reads manufacturing batches, handles missing data artifacts caused by factory floor logging anomalies, and utilizes vectorized NumPy arrays to monitor waste ratios against environmental compliance targets.

## 🛠️ Key Technical Implementations

### 1. Vectorized Mass Balancing
To process continuous industrial logs instantly without relying on computationally expensive Python loops, raw factory matrices are transformed into memory-mapped arrays. Waste indexes are computed via parallel vector division math:
⁠ python
df['Waste_Percentage'] = (scrap_array / total_mass_array) * 100

### 2. Failure-Safe Factory Imputation
Industrial environments are highly prone to data omissions due to hardware telemetry issues. The system intercepts missing observations (⁠ NaN ⁠) using safe statistical imputation mechanics via Pandas (⁠ .fillna() ⁠) to preserve ledger matrix structures prior to system auditing.

### 3. Sustainability Boundary Flagging
Aligned with sustainable manufacturing protocols, the pipeline leverages NumPy's optimized ⁠ np.where() ⁠ framework to flag batches violating clean production limits (> 8% scrap metrics) without incurring iteration overhead.

## 🚀 Execution Instructions

1.⁠ ⁠Clone this repository to your system workspace:
   ⁠ bash
   git clone https://github.com
   cd plastic-factory-defect-tracker
    ⁠

2.⁠ ⁠Run the analytical optimization script:
   ⁠ bash
   python src/factory_analyzer.py
    ⁠

## 📊 Sample Program Outputs
Running the factory code dynamically cleans the production logs and populates the console window with high-level key performance metrics:
•⁠  ⁠*Total Raw Material Intake*: Comprehensive polymer mass consumed (KG)
•⁠  ⁠*Aggregated Material Loss Index*: Mass totals isolated to scrap bins (KG)
•⁠  ⁠*Polymer Efficiencies*: Structural performance breakdown mapping out which plastic compositions (PET, PP, HDPE) optimize clean manufacturing.
