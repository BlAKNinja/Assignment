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
cd ProducerConsumerSystem
```

Run:
```
python producer_consumer/main.py
```

This demonstrates:
- Custom BlockingQueue implementation  
- Thread synchronization (wait/notify)  
- Producer and Consumer thread communication  

---

## ▶️ **How to Run Assignment 2 (Sales Data Analysis)**

Navigate to:
```
cd Assignment2_DataAnalysis
```

Run:
```
python sales_analysis/main.py
```

This will:
- Load `sample_sales.csv`
- <img width="682" height="608" alt="image" src="https://github.com/user-attachments/assets/4128fb75-bffb-4308-a087-3e9656813618" />

- Compute:
  - Total revenue  
  - Total quantity  
  - Revenue by region  
  - Top-selling products  
- Print results to the console  
- <img width="1270" height="118" alt="image" src="https://github.com/user-attachments/assets/45b3b79d-0d1f-49e3-8b89-16822d32d532" />


---

## 🧪 **Running Unit Tests**

### Assignment 1:
```
cd ProducerConsumerSystem
python -m unittest discover -s tests -v
```

### Assignment 2:
```
cd Assignment2_DataAnalysis
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
<img width="1702" height="742" alt="image" src="https://github.com/user-attachments/assets/7f1bf234-bb08-453b-90a4-024d9e983b09" />


### Assignment 2 – Sales Analysis Output
<img width="682" height="608" alt="image" src="https://github.com/user-attachments/assets/1d5a7078-02a4-497e-8b63-78930b99a6d0" />
- <img width="1270" height="118" alt="image" src="https://github.com/user-attachments/assets/45b3b79d-0d1f-49e3-8b89-16822d32d532" />


---

## 🧑‍💻 **About This Repository**

- Clean modular architecture  
- Fully tested using `unittest`  
- Demonstrates Python threading, synchronization, functional programming, CSV processing, and aggregation  
- Suitable for academic submission or portfolio work  

---

## 📜 **License**
Open for educational use.
