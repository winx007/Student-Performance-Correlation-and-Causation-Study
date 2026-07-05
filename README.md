# Student Performance Analysis Dashboard

This repository contains the Week 1 Project for Data Science Internship (Name: Muhammad Waleed, Roll No: Mtech-DS26026).

## Project Overview
**Topic:** Correlation & Causation Study
**Goal:** Analyze relationships in student data (Study time vs Grades, Sleep vs Performance).

## Folder Structure
- `data/` - Contains the raw and cleaned synthetic datasets.
- `notebooks/` - Contains `analysis.ipynb` for EDA and statistical modeling.
- `scripts/` - Contains data generation scripts.
- `visualizations/` - Contains the `dashboard.py` (Modern Tkinter GUI).

## How to Run

1. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate Data (Optional, already provided):**
   ```bash
   python scripts/generate_data.py
   ```

3. **Run Dashboard:**
   ```bash
   python visualizations/dashboard.py
   ```
   The dashboard features a modern interface with Light/Dark mode support. Select different variables from the sidebar to view their correlation with GPA.

4. **View Notebook:**
   Open `notebooks/analysis.ipynb` in Jupyter or VS Code to see the step-by-step data cleaning and exploratory analysis.

## Deliverables Checklist
- [x] Jupyter Notebook with full analysis
- [x] Clean dataset
- [x] Interactive Dashboard (Tkinter/CustomTkinter)
- [x] GitHub repository structure
- [x] Project Report (`report.md` -> export to PDF)
