#  Stock Portfolio Tracker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Project-Stock%20Portfolio%20Tracker-success?style=for-the-badge" alt="Project">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/CodeAlpha-Internship-FF6B00?style=for-the-badge" alt="CodeAlpha">
</p>

<p align="center">
  A practical <strong>console-based Stock Portfolio Tracker</strong> built with Python.<br>
  Calculate investment values based on predefined stock prices and securely store portfolio records.
</p>

---

## 📖 Overview

The **Stock Portfolio Tracker** is a lightweight Python application designed to help users calculate the total value of their stock investments.

The program uses a predefined dictionary containing stock prices and allows users to enter stock symbols along with quantities owned. Based on the provided input, it computes the total investment value and stores the transaction details in an external text file for future reference.

This project demonstrates essential Python programming concepts such as **dictionary operations, file handling, input processing, and basic financial calculations**.

---

## ✨ Features

-  **Predefined Stock Price Database** using a hardcoded dictionary of stock values.
-  **Case-Insensitive Ticker Input** allowing users to enter stock symbols in any letter case.
-  **Automatic Investment Calculation** to instantly determine total portfolio value.
-  **Persistent Record Storage** by saving portfolio details to `portfolio.txt`.
-  **Input Validation** that gracefully handles unavailable stock symbols.

---

## 🖥️ Application Preview

### Terminal Interface

```text
Enter stock name: aapl
Enter quantity: 6

Total investment value: 1080
Result saved in portfolio.txt
```

### Sample Output (`portfolio.txt`)

```text
Stock: AAPL
Quantity: 6
Investment Value: 1080
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| Dictionaries | Store stock prices and mappings |
| File I/O | Save portfolio records permanently |
| Type Casting | Process and validate user inputs |

---

## 📂 Project Structure

```text
Task2_Stock Portfolio Tracker/
│
├── main.py           # Main application script
├── portfolio.txt     # Stores portfolio records
└── README.md         # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AqsaAliRazaJamali/CodeAlpha_Stock_Portfolio_Tracker.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd CodeAlpha_Stock_Portfolio_Tracker
```

### 3️⃣ Run the Application

```bash
python main.py
```

---

## 📚 Concepts Demonstrated

This project showcases several fundamental Python concepts, including:

- Dictionary Data Structures
- User Input Handling
- String Manipulation (`.upper()`)
- Type Conversion (`int()`)
- Conditional Statements (`if-else`)
- Basic Arithmetic Operations
- File Handling using `with open()`
- Data Persistence using Append Mode (`"a"`)

---

## 🎓 Internship Information

This project was completed as **Task 2** of the **Python Programming Internship** offered by **CodeAlpha**.

---

## 👩‍💻 Author

<div align="center">

### **Aqsa Jamali**

[![GitHub](https://img.shields.io/badge/GitHub-AqsaAliRazaJamali-181717?style=for-the-badge&logo=github)](https://github.com/AqsaAliRazaJamali)

</div>

---

<div align="center">

⭐ If you found this project useful, consider giving it a star!

</div>
