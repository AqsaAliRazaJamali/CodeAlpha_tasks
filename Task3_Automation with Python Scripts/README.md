# 📧 Automated Email Extractor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Project-Email%20Extractor-success?style=for-the-badge" alt="Project">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/CodeAlpha-Internship-FF6B00?style=for-the-badge" alt="CodeAlpha">
</p>

<p align="center">
  A smart <strong>Python-powered automation script</strong> that extracts email addresses from unstructured text files.<br>
  Eliminate manual searching by automatically identifying, filtering, and organizing email data in seconds.
</p>

---

## 📖 Overview

The **Automated Email Extractor** is a practical Python automation tool designed to process raw text files and extract valid email addresses efficiently.

Using **Regular Expressions (`re`)**, the script scans unstructured text, identifies email patterns, removes duplicate entries using Python sets, and saves the cleaned results into a dedicated output file.

This project demonstrates essential concepts in **task automation, text processing, pattern matching, and file handling**.

---

## ✨ Features

-  **Automated Text Scanning** to search through unstructured text files.
-  **Regex-Based Email Extraction** using Python's `re` module.
-  **Duplicate Removal** through Python `set` operations.
-  **Console Output Display** for immediate viewing of extracted emails.
-  **Automatic File Generation** that stores extracted emails in `emails.txt`.

---

## 🖥️ Preview Demo

### Sample Input (`sample.txt`)

```text
Hello everyone,
Contact us at support@gmail.com
For internships: internship@codealpha.tech
For complaints: helpdesk@yahoo.com
```

### Terminal Output

```text
Extracted Email Address:

internship@codealpha.tech
helpdesk@yahoo.com
support@gmail.com

Emails saved successfully in emails.txt
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| `re` Module | Regular expression pattern matching |
| Sets | Duplicate removal and data filtering |
| File I/O | Reading input files and writing output files |

---

## 📂 Project Structure

```text
Task3_Automation with Python Scripts/
│
├── email_extractor.py   # Main automation script
├── sample.txt           # Input file containing raw text
├── emails.txt           # Generated file with extracted emails
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AqsaAliRazaJamali/CodeAlpha_Email_Extractor.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd CodeAlpha_Email_Extractor
```

### 3️⃣ Run the Script

```bash
python email_extractor.py
```

---

## 📚 Concepts Demonstrated

This project showcases several fundamental Python concepts, including:

- Regular Expressions using `re.findall()`
- File Handling (`open()`, `read()`, `write()`)
- Data Deduplication using Python `set`
- String Processing and Pattern Recognition
- Looping and Data Iteration
- Console-Based Output Formatting

---

## 🎓 Internship Information

This project was completed as **Task 3** of the **Python Programming Internship** offered by **CodeAlpha**.

---

## 👩‍💻 Author

<div align="center">

### **Aqsa Jamali**

[![GitHub](https://img.shields.io/badge/GitHub-AqsaAliRazaJamali-181717?style=for-the-badge&logo=github)](https://github.com/AqsaAliRazaJamali)

</div>

---

<div align="center">

⭐ If you found this project helpful, consider giving it a star!

</div>
