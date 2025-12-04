# 📘 **Python Assignments – Producer–Consumer & Sales Data Analysis**

This repository contains two complete Python assignments packaged together: **Assignment 1 – Producer–Consumer System (Thread Synchronization)** and **Assignment 2 – Sales Data Analysis (Functional Programming & Aggregation)**. Both assignments follow clean modular architecture and include full unit test coverage.

---


## ⚙️ **Setup Instructions**

### 1️⃣ Install Python (3.9+ recommended)

Check version:
```
python --version
```

### 2️⃣ Install dependencies (optional for coverage)
```
pip install coverage
```

---

## ▶️ **How to Run Assignment 1 (Producer–Consumer System)**

Navigate to:
```
cd assignment1_producer_consumer
```

Run:
```
python src/producer_consumer/main.py
```

This demonstrates:
- Custom BlockingQueue implementation  
- Thread synchronization (wait/notify)  
- Producer and Consumer thread communication  

---

## ▶️ **How to Run Assignment 2 (Sales Data Analysis)**

Navigate to:
```
cd assignment2_data_analysis
```

Run:
```
python src/sales_analysis/main.py
```

This will:
- Load `sample_sales.csv`
- Compute:
  - Total revenue  
  - Total quantity  
  - Revenue by region  
  - Top-selling products  
- Print results to the console  
- *(Screenshots to be added)*

---

## 🧪 **Running Unit Tests**

### Assignment 1:
```
cd assignment1_producer_consumer
python -m unittest discover -s tests -v
```

### Assignment 2:
```
cd assignment2_data_analysis
python -m unittest discover -s tests -v
```

---

## 📈 **Generate Coverage Report (Optional)**

Run with coverage:
```
coverage run -m unittest discover -s tests
```

Show terminal report:
```
coverage report -m
```

Generate HTML report:
```
coverage html
```

Open report:
```
open htmlcov/index.html
```

---

## 🖼 **Output Screenshots**

### Assignment 1 – Producer–Consumer Output
*(Insert screenshot here)*

### Assignment 2 – Sales Analysis Output
*(Insert screenshot here)*

---

## 🧑‍💻 **About This Repository**

- Clean modular architecture  
- Fully tested using `unittest`  
- Demonstrates Python threading, synchronization, functional programming, CSV processing, and aggregation  
- Suitable for academic submission or portfolio work  

---

## 📜 **License**
Open for educational use.
