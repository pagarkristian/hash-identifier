<h1 align="center">🛡️ Hash Identifier</h1>
<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Version-2.0-orange?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Field-Cybersecurity-red?style=for-the-badge" alt="Category">
  <img src="https://img.shields.io/badge/Tests-25%20Passed-brightgreen?style=for-the-badge" alt="Tests">
</div>

**Hash Identifier** is a Python-based Command Line Interface (CLI) tool designed to identify common cryptographic hash algorithms using pattern matching and length validation.

This project was developed as a cybersecurity learning project to help students, CTF participants, and security enthusiasts quickly classify unknown hash values.

---

## 🚀 Features

<table>
  <thead>
    <tr>
      <th width="25%">Category</th>
      <th width="30%">Feature</th>
      <th width="45%">Technical Capabilities</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="10" align="center"> <br><b>Core Engine</b></td>
      <td><code>Regex Pattern Matching</code></td>
      <td>Uses optimized regular expressions for instant and accurate hash type identification.</td>
    </tr>
    <tr>
      <td><code>MD5</code></td>
      <td>Identifies 128-bit MD5 hashes.</td>
    </tr>
    <tr>
      <td><code>SHA-1</code></td>
      <td>Detects 160-bit SHA-1 cryptographic hashes.</td>
    </tr>
    <tr>
      <td><code>SHA-224</code></td>
      <td>Validates SHA-2 family 224-bit hashes.</td>
    </tr>
    <tr>
      <td><code>SHA-256</code></td>
      <td>Validates SHA-2 family 256-bit hashes.</td>
    </tr>
    <tr>
      <td><code>SHA-384</code></td>
      <td>Supports high-security SHA-2 family 384-bit hashes.</td>
    </tr>
    <tr>
      <td><code>SHA-512</code></td>
      <td>Supports high-security SHA-2 family 512-bit hashes.</td>
    </tr>
    <tr>
      <td><code>bcrypt</code> 🆕</td>
      <td>Detects bcrypt password hashes ($2a$, $2b$, $2y$ prefix).</td>
    </tr>
    <tr>
      <td><code>SHA512crypt</code> 🆕</td>
      <td>Detects Unix SHA512crypt password hashes ($6$ prefix).</td>
    </tr>
    <tr>
      <td><code>Argon2</code> 🆕</td>
      <td>Detects Argon2 password hashes ($argon2i$, $argon2d$, $argon2id$ prefix).</td>
    </tr>
    <tr>
      <td rowspan="2" align="center"> <br><b>Scanning Modes</b></td>
      <td>Single Hash Analysis</td>
      <td>Quick analysis for a single hash input via CLI.</td>
    </tr>
    <tr>
      <td>Batch Scanning</td>
      <td>Bulk processing by importing and parsing hashes from <code>.txt</code> files.</td>
    </tr>
    <tr>
      <td rowspan="5" align="center"> <br><b>Data & Output</b></td>
      <td>TXT Report</td>
      <td>Generates clean, human-readable text summaries with timestamp and hash length.</td>
    </tr>
    <tr>
      <td>JSON Export</td>
      <td>Exports structured JSON data including timestamp, hash length, and confidence level.</td>
    </tr>
    <tr>
      <td>CSV Export 🆕</td>
      <td>Exports scan results to CSV format for spreadsheet analysis.</td>
    </tr>
    <tr>
      <td>Activity Logging</td>
      <td>Records scan history and identified hash types.</td>
    </tr>
    <tr>
      <td>Statistics Module</td>
      <td>Displays detection rate, most common hash, confidence breakdown, and hash type distribution.</td>
    </tr>
    <tr>
      <td rowspan="2" align="center"> <br><b>Validation</b></td>
      <td>Dynamic Confidence Scoring</td>
      <td>Assigns <code>High</code> confidence for unique-length hashes and <code>Medium</code> for ambiguous lengths.</td>
    </tr>
    <tr>
      <td>Input Validation</td>
      <td>Detects empty input and handles whitespace stripping before analysis.</td>
    </tr>
    <tr>
      <td rowspan="4" align="center"> <br><b>User Interface</b></td>
      <td>Interactive CLI Menu</td>
      <td>User-friendly, keyboard-navigable terminal menu with 6 options.</td>
    </tr>
    <tr>
      <td>Colored Terminal Output 🆕</td>
      <td>Confidence results displayed in color: 🟢 High, 🟡 Medium, 🔴 Low.</td>
    </tr>
    <tr>
      <td>View Latest Report 🆕</td>
      <td>Display the latest scan report directly in the terminal.</td>
    </tr>
    <tr>
      <td>Scan History Viewer 🆕</td>
      <td>View and clear scan history from the CLI menu.</td>
    </tr>
    <tr>
      <td align="center"> <br><b>Testing</b></td>
      <td>Unit Test Suite</td>
      <td>25 automated tests covering detector, password hash, batch scan, logger, and report modules.</td>
    </tr>
  </tbody>
</table>

---

## 📂 Project Structure

```text
hash-identifier/
│
├── examples/
│   └── hashes.txt
│
├── logs/
│   └── hash_identifier.log
│
├── reports/
│   ├── report.csv
│   ├── report.json
│   ├── report.txt
│   └── stats.json
│
├── screenshots/
│
├── src/
│   ├── banner.py
│   ├── batch_scan.py
│   ├── detector.py
│   ├── history.py
│   ├── logger.py
│   ├── main.py
│   ├── patterns.py
│   ├── report.py
│   └── stats.py
│
├── tests/
│   ├── test_batch.py
│   ├── test_detector.py
│   ├── test_logger.py
│   └── test_report.py
│
├── conftest.py
├── README.md
└── LICENSE
```

---

## 🔍 Supported Algorithms

### Cryptographic Hashes

| Algorithm | Length (Chars) | Character Set | Confidence | Format Example |
| :--- | :---: | :---: | :---: | :--- |
| `MD5` | **32** | Hexadecimal | 🟢 High | `5f4dcc3b5aa765d61d8327deb882cf99` |
| `SHA-1` | **40** | Hexadecimal | 🟢 High | `aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d` |
| `SHA-224` | **56** | Hexadecimal | 🟡 Medium | `ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193` |
| `SHA-256` | **64** | Hexadecimal | 🟡 Medium | `2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824` |
| `SHA-384` | **96** | Hexadecimal | 🟡 Medium | `59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f` |
| `SHA-512` | **128** | Hexadecimal | 🟡 Medium | `9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043` |

### Password Hashes 🆕

| Algorithm | Prefix | Confidence | Format Example |
| :--- | :---: | :---: | :--- |
| `bcrypt` | `$2a$` `$2b$` `$2y$` | 🟢 High | `$2b$12$KIXyZfVqJWJmPMBYMJFqOe...` |
| `SHA512crypt` | `$6$` | 🟢 High | `$6$rounds=5000$usesomesillystri$D4Irl...` |
| `Argon2` | `$argon2i$` `$argon2d$` `$argon2id$` | 🟢 High | `$argon2id$v=19$m=65536,t=2,p=1$...` |

---

## 🚀 Installation

Follow these steps to get the environment ready and run the tool on your local machine.

### Prerequisites
Make sure **Git** and **Python 3** are provisioned on your current deployment environment (e.g., Kali Linux, Parrot OS, or Ubuntu/WSL).

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/pagarkristian/hash-identifier.git
```

```bash
# 2. Move into the project directory
cd hash-identifier
```

```bash
# 3. Launch the tool
python3 -m src.main
```

---

## 💡 Usage

🔹 **1: Single Hash Verification**

```plaintext
Enter Hash: 5f4dcc3b5aa765d61d8327deb882cf99

Analysis Result
==================================================
Hash Length: 32
Hash Type  : MD5
Description: Message Digest Algorithm 5
Confidence : High
Report File: reports/report.txt
```

🔹 **2: Batch Scan From File**

```plaintext
[1] MD5 (32 chars)
[2] SHA256 (64 chars)

==================================================
Batch Scan Summary
==================================================
Total Hashes   : 2
Detected       : 2
Unknown        : 0
Detection Rate : 100.00%
Most Common Hash : MD5
```

🔹 **3: View Statistics**

```plaintext
Statistics
==================================================
Total Hashes Scanned : 22
Detected             : 22
Unknown              : 0
Detection Rate       : 100.00%
Most Common Hash     : MD5

Hash Type Breakdown
==================================================
MD5          : 21 (95.45%)
SHA256       : 1 (4.55%)

Confidence Breakdown
==================================================
High   : 21
Medium : 1
Low    : 0
```

🔹 **Password Hash Detection**

```plaintext
Enter Hash: $2b$12$KIXyZfVqJWJmPMBYMJFqOeGkmFpPHQxGQoAZWvRFdaFCRrFP9fIHi

Analysis Result
==================================================
Hash Length: 60
Hash Type  : bcrypt
Description: bcrypt Password Hash
Confidence : High
Report File: reports/report.txt
```

---

## 📝 Reports

After each scan, the application generates reports inside: `reports/`

#### 1. Plaintext Report (`report.txt`)
```text
HASH IDENTIFIER REPORT
==================================================
Timestamp  : 2026-06-07 00:01:22
Hash Value : 5f4dcc3b5aa765d61d8327deb882cf99
Hash Length: 32
Hash Type  : MD5
Description: Message Digest Algorithm 5
Confidence : High
```

#### 2. JSON Report (`report.json`)
```json
{
  "timestamp": "2026-06-07 00:01:22",
  "hash_value": "5f4dcc3b5aa765d61d8327deb882cf99",
  "hash_length": 32,
  "hash_type": "MD5",
  "description": "Message Digest Algorithm 5",
  "confidence": "High"
}
```

#### 3. CSV Export (`report.csv`)
```text
timestamp,hash_value,hash_length,hash_type,confidence
2026-06-07 00:01:22,5f4dcc3b5aa765d61d8327deb882cf99,32,MD5,High
```

---

## Logging

The application automatically saves your scan history so you can check your past work anytime.

| File Name | Location | What it does |
| :--- | :--- | :--- |
| 📋 **Activity Log** | `logs/hash_identifier.log` | Saves the history of all the hashes you have scanned. |

### 📝 Example Log

```text
[2026-06-07 21:16:52] HASH=$2b$12$KIXyZfVqJWJmPMBYMJFqOeGkmFpPHQxGQoAZWvRFdaFCRrFP9fIHi TYPE=bcrypt
[2026-06-07 21:28:54] HASH=$6$rounds=5000$usesomesillystri$D4Irl... TYPE=SHA512crypt
[2026-06-07 21:34:18] HASH=$argon2id$v=19$m=65536,t=2,p=1$... TYPE=Argon2
```

---

##  Testing

This project includes a full automated test suite using **pytest**.

```bash
pytest tests/ -v
```

```text
tests/test_batch.py::test_scan_file_valid                    PASSED
tests/test_batch.py::test_scan_file_not_found               PASSED
tests/test_batch.py::test_scan_file_empty                   PASSED
tests/test_detector.py::test_md5                            PASSED
tests/test_detector.py::test_sha1                           PASSED
tests/test_detector.py::test_sha224                         PASSED
tests/test_detector.py::test_sha256                         PASSED
tests/test_detector.py::test_sha384                         PASSED
tests/test_detector.py::test_sha512                         PASSED
tests/test_detector.py::test_unknown                        PASSED
tests/test_detector.py::test_empty_string                   PASSED
tests/test_detector.py::test_whitespace_stripped            PASSED
tests/test_detector.py::test_bcrypt                         PASSED
tests/test_detector.py::test_sha512crypt                    PASSED
tests/test_detector.py::test_argon2                         PASSED
tests/test_detector.py::test_password_hash_returns_none_for_md5  PASSED
tests/test_logger.py::test_write_log_creates_file           PASSED
tests/test_logger.py::test_write_log_contains_hash          PASSED
tests/test_logger.py::test_write_log_contains_type          PASSED
tests/test_report.py::test_save_report_txt                  PASSED
tests/test_report.py::test_save_report_json                 PASSED
tests/test_report.py::test_save_report_has_timestamp        PASSED
tests/test_report.py::test_save_report_has_hash_length      PASSED
tests/test_report.py::test_save_report_confidence_high      PASSED
tests/test_report.py::test_save_report_returns_path         PASSED

25 passed in 0.08s
```

---

## Current Version

| Version | Status | Implemented Features |
| :---: | :---: | :--- |
| **v1.1** | ✅ Stable | • Hash Detection Engine<br>• Batch Scan Module<br>• TXT Report Export<br>• JSON Report Export<br>• Logging System<br>• Command Line Interface<br>• Colored Banner |
| **v2.0** | ✅ Stable | • bcrypt Detection<br>• SHA512crypt Detection<br>• Argon2 Detection<br>• Dynamic Confidence Scoring (High/Medium/Low)<br>• Colorized Terminal Output<br>• CSV Export<br>• View Latest Report Menu<br>• Scan History Viewer<br>• Clear History Menu<br>• Improved Statistics Module<br>• Improved Reporting (Timestamp + Hash Length)<br>• Unit Test Suite (25/25 Passed) |

---

> 💡 **Note:** All features listed above are fully tested and ready to use. More updates and new features will be added in future versions!

## Project Roadmap

| Target Version | Status | Planned Features & Goals |
| :---: | :---: | :--- |
| **v2.0** | ✅ Complete | • Password Hash Detection (bcrypt, SHA512crypt, Argon2)<br>• Dynamic Confidence Scoring<br>• Colorized Output<br>• CSV Export<br>• View Latest Report<br>• Scan History Viewer<br>• Unit Test Suite (25/25 Passed) |
| **v3.0** | 🔵 Future | • Introduce REST API support<br>• Implement plugin architecture<br>• Provide Docker deployment setup<br>• Create a lightweight web interface for remote analysis |

---

## 📸 Screenshots

Here are the visual previews of the tool in action:

| Preview Type | Screenshot | Status |
| :--- | :---: | :---: |
| 🖥️ **Main Menu Interface** |<img src="https://github.com/user-attachments/assets/2dcf9aed-061d-4bb5-b5e7-e141546e0e02" width="400" alt="Main Menu Interface">| ✅ Available |
| 🔐 **bcrypt Detection** | <img src="https://github.com/user-attachments/assets/6415cea8-876e-40cd-ba5d-209c4283620d" width="400" alt="bcrypt"> | ✅ Available |
| 🔐 **SHA512crypt Detection** | <img src="https://github.com/user-attachments/assets/5881b5a7-097c-4d5d-8030-1b5b00a4412c" width="400" alt="SHA512crypt"> | ✅ Available |
| 🔐 **Argon2 Detection** | <img src="https://github.com/user-attachments/assets/955aa5a7-f819-4c83-84e2-f6353a8cf480" width="400" alt="Argon2"> | ✅ Available |
| 📄 **View Latest Report** | <img src="https://github.com/user-attachments/assets/58e0a578-1629-49d5-a220-5380118ea451" width="400" alt="Latest Report"> | ✅ Available |
| 📋 **Scan History Viewer** | <img src="https://github.com/user-attachments/assets/1bc97ead-ec10-4efe-870d-3d5c83290635" width="400" alt="Scan History"> | ✅ Available |
| 🔍 **Batch Scanning Mode** | <img src="https://github.com/user-attachments/assets/a7762211-165d-4a7a-adfb-6397beb62bd7" width="300" alt="Batch Scan 1"><br><br><img src="https://github.com/user-attachments/assets/489fbffc-ca44-4bdb-98d8-3922c4fd7bcf" width="300" alt="Batch Scan 2"> | ✅ Available |
|  **View Statistics** | <img src="https://github.com/user-attachments/assets/b8ffd280-7b48-44cb-8829-c98c185038c7" width="400" alt="Statistics"> | ✅ Available |
|  **Unit Testing** | <img src="https://github.com/user-attachments/assets/5182caf3-c775-4886-91d9-f0ddf51cb520" width="400" alt="Pytest"> | ✅ Available |
| 📋 **Activity Log** | <img src="https://github.com/user-attachments/assets/88a3026f-8b26-4ea7-acb7-91953481cbfe" width="400" alt="Log"> | ✅ Available |

---

## 📄 License

This project is licensed under the **MIT License**. This means you are free to use, modify, and distribute this software for personal or educational purposes.

---

## 👨‍💻 Author

<div align="center">
  <h3>pagarkristian</h3>
  <p>Cybersecurity Student • Python Learner • Open Source Enthusiast</p>
</div>
