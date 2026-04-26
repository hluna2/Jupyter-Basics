# Jupyter Notebook

A beginner-friendly project demonstrating how Jupyter Notebook works. Jupyter is an interactive computing environment that is very commonly used in data science and analytics while also allowing for other functions like documentation. Using Python, this project features Titanic data visualization and async programming examples to show Jupyter's versatility beyond just data science.

## Overview

This project covers:
- How Jupyter Notebook works (cells, kernel, execution order)
- Data loading, cleaning, and visualization with Titanic data
- Async functions in Jupyter - Not just for data science
- Flask API served from background thread inside Jupyter


## Project Structure

```
BasicsOfJupyter/
├── notebooks/
│   ├── 01_Basics.ipynb       # how jupyter works
│   ├── 02_Charts.ipynb       # data viz + flask api
│   └── 03_Async.ipynb        # async example
├── venv
├── app.py                    # flask api and background thread
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.10+
- Jupyter Notebook


## Setup

```bash
git clone https://github.com/you/project
cd project
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

## Notebooks
01 — Jupyter Basics

- Cells: code vs markdown
- Execution order and the kernel
- Shortcuts and tips  

02 — Titanic Charts

- Dataset loaded directly
- Data inspection: shape, columns, null checks
- Flask API running in a background thread
- Fetching API responses via `requests.get()`
- Survival rate by passenger class (bar chart)
- Fare distribution by class (box plot, log scale)  

03 — Async Demo

- Using `await` directly at the top level
- Running concurrent tasks with `asyncio.gather()`

---

## Data
Titanic dataset loaded directly from seaborn via `sns.load_dataset('titanic')`. No file download or setup required.