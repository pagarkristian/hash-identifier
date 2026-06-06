<h1 align="center">🛡️ Hash Identifier</h1>
<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Version-2.0-orange?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Field-Cybersecurity-red?style=for-the-badge" alt="Category">
  <img src="https://img.shields.io/badge/Tests-23%20Passed-brightgreen?style=for-the-badge" alt="Tests">
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
      <td rowspan="11" align="center"> <br><b>Core Engine</b></td>
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
      <td><code>SHA3-224</code> 🆕</td>
      <td>Identifies SHA-3 family 224-bit hashes.</td>
    </tr>
    <tr>
      <td><code>SHA3-256</code> 🆕</td>
      <td>Identifies SHA-3 family 256-bit hashes.</td>
    </tr>
    <tr>
      <td><code>SHA3-384</code> 🆕</td>
      <td>Identifies SHA-3 family 384-bit hashes.</td>
    </tr>
    <tr>
      <td><code>SHA3-512</code> 🆕</td>
      <td>Identifies SHA-3 family 512-bit hashes.</td>
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
      <td rowspan="4" align="center"> <br><b>Data & Output</b></td>
      <td>TXT Report</td>
      <td>Generates clean, human-readable text summaries with timestamp and hash length.</td>
    </tr>
    <tr>
      <td>JSON Export</td>
      <td>Exports structured JSON data including timestamp, hash length, and confidence level.</td>
    </tr>
    <tr>
      <td>Activity Logging</td>
      <td>Records scan history and identified hash types.</td>
    </tr>
    <tr>
      <td>Statistics Module 🆕</td>
      <td>Displays detection rate, most common hash, confidence breakdown, and hash type distribution.</td>
    </tr>
    <tr>
      <td rowspan="2" align="center"> <br><b>Validation</b></td>
      <td>Dynamic Confidence Scoring 🆕</td>
      <td>Assigns <code>High</code> confidence for unique-length hashes and <code>Medium</code> for ambiguous lengths.</td>
    </tr>
    <tr>
      <td>Input Validation 🆕</td>
      <td>Detects empty input and handles whitespace stripping before analysis.</td>
    </tr>
    <tr>
      <td rowspan="2" align="center"> <br><b>User Interface</b></td>
      <td>Interactive CLI Menu</td>
      <td>User-friendly, keyboard-navigable terminal menu.</td>
    </tr>
    <tr>
      <td>Colored Terminal Banner</td>
      <td>Styled with vibrant ANSI colors for a premium CLI look.</td>
    </tr>
    <tr>
      <td align="center"> <br><b>Testing</b></td>
      <td>Unit Test Suite 🆕</td>
      <td>23 automated tests covering detector, batch scan, logger, and report modules.</td>
    </tr>
  </tbody>
</table>

---

##  Project Structure

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

##  Supported Algorithms

The tool uses precise cryptographic patterns to identify hashes based on their structural properties:

| Algorithm | Length (Chars) | Character Set | Confidence | Format Example |
| :--- | :---: | :---: | :---: | :--- |
| `MD5` | **32** | Hexadecimal | 🟢 High | `5f4dcc3b5aa765d61d8327deb882cf99` |
| `SHA-1` | **40** | Hexadecimal | 🟢 High | `aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d` |
| `SHA-224` | **56** | Hexadecimal | 🟡 Medium | `ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193` |
| `SHA-256` | **64** | Hexadecimal | 🟡 Medium | `2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824` |
| `SHA-384` | **96** | Hexadecimal | 🟡 Medium | `59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f` |
| `SHA-512` | **128** | Hexadecimal | 🟡 Medium | `9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043` |
| `SHA3-224` 🆕 | **56** | Hexadecimal | 🟡 Medium | `ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193` |
| `SHA3-256` 🆕 | **64** | Hexadecimal | 🟡 Medium | `a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a` |
| `SHA3-384` 🆕 | **96** | Hexadecimal | 🟡 Medium | `ec01498288516fc926459f58e2c6ad8df9b473cb0fc08c2596da7cf0e49be4b298d88cea927ac7f539f1edf228376d25` |
| `SHA3-512` 🆕 | **128** | Hexadecimal | 🟡 Medium | `a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26` |

> 💡 **Note:** SHA-2 and SHA-3 share the same length and character set, so they cannot be distinguished by pattern matching alone. The tool will return the SHA-2 variant with Medium confidence for ambiguous lengths.

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
==================================================
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

---

## Logging

The application automatically saves your scan history so you can check your past work anytime.

| File Name | Location | What it does |
| :--- | :--- | :--- |
| 📋 **Activity Log** | `logs/hash_identifier.log` | Saves the history of all the hashes you have scanned. |

### 📝 Example Log

```text
[2026-06-04 21:15:30] HASH=5f4dcc3b5aa765d61d8327deb882cf99 TYPE=MD5
[2026-06-04 21:16:02] HASH=aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d TYPE=SHA-1
```

---

##  Testing

This project includes a full automated test suite using **pytest**.

```bash
pytest tests/ -v
```

```text
tests/test_batch.py::test_scan_file_valid        PASSED
tests/test_batch.py::test_scan_file_not_found    PASSED
tests/test_batch.py::test_scan_file_empty        PASSED
tests/test_detector.py::test_md5                 PASSED
tests/test_detector.py::test_sha1                PASSED
tests/test_detector.py::test_sha224              PASSED
tests/test_detector.py::test_sha256              PASSED
tests/test_detector.py::test_sha384              PASSED
tests/test_detector.py::test_sha512              PASSED
tests/test_detector.py::test_unknown             PASSED
tests/test_detector.py::test_empty_string        PASSED
tests/test_detector.py::test_whitespace_stripped PASSED
tests/test_detector.py::test_sha3_256            PASSED
tests/test_detector.py::test_sha3_512            PASSED
tests/test_logger.py::test_write_log_creates_file    PASSED
tests/test_logger.py::test_write_log_contains_hash   PASSED
tests/test_logger.py::test_write_log_contains_type   PASSED
tests/test_report.py::test_save_report_txt           PASSED
tests/test_report.py::test_save_report_json          PASSED
tests/test_report.py::test_save_report_has_timestamp PASSED
tests/test_report.py::test_save_report_has_hash_length  PASSED
tests/test_report.py::test_save_report_confidence_high  PASSED
tests/test_report.py::test_save_report_returns_path  PASSED

23 passed in 0.04s
```

---

## Current Version

| Version | Status | Implemented Features |
| :---: | :---: | :--- |
| **v1.1** | ✅ Stable | • Hash Detection Engine<br>• Batch Scan Module<br>• TXT Report Export<br>• JSON Report Export<br>• Logging System<br>• Command Line Interface<br>• Colored Banner |
| **v2.0** | ✅ Stable | • SHA-3 Family Support (SHA3-224/256/384/512)<br>• Dynamic Confidence Scoring (High/Medium/Low)<br>• Improved Statistics Module<br>• Improved Reporting System (Timestamp + Hash Length)<br>• Unit Test Suite (23/23 Passed) |

---

> 💡 **Note:** All features listed above are fully tested and ready to use. More updates and new features will be added in future versions!

## Project Roadmap

| Target Version | Status | Planned Features & Goals |
| :---: | :---: | :--- |
| **v3.0** | 🔵 Future | • Introduce REST API support<br>• Implement plugin architecture<br>• Provide Docker deployment setup<br>• Create a lightweight web interface for remote analysis |

---

## 📸 Screenshots

Here are the visual previews of the tool in action:

| Preview Type | Screenshot | Status |
| :--- | :---: | :---: |
|  **Main Menu Interface** | <img src="https://github.com/user-attachments/assets/844e2862-62c5-47b8-a762-8c9ebf86b5a1" width="400" alt="Main Menu"> | ✅ Available |
|  **Single Hash Scan** | <img src="https://github.com/user-attachments/assets/e7bbd34c-82b5-4b79-b748-719c7eaf017d" width="400" alt="Single Scan"> | ✅ Available |
|  **Batch Scanning Mode** | <img src="https://github.com/user-attachments/assets/a7762211-165d-4a7a-adfb-6397beb62bd7" width="300" alt="Batch Scan 1"><br><br><img src="https://github.com/user-attachments/assets/489fbffc-ca44-4bdb-98d8-3922c4fd7bcf" width="300" alt="Batch Scan 2"> | ✅ Available |
|  **View Statistics** | <img src="https://github.com/user-attachments/assets/b8ffd280-7b48-44cb-8829-c98c185038c7" width="400" alt="Statistics"> | ✅ Available |
|  **Report Generation** | <img src="https://github.com/user-attachments/assets/450b9306-abb3-4f1e-8d14-7105fc804f85" width="400" alt="Report TXT"><br><br><img src="https://github.com/user-attachments/assets/18176643-07f2-4db8-8937-e02b94e60a4c" width="400" alt="Report JSON"> | ✅ Available |
|  **Unit Testing** | <img src="https://github.com/user-attachments/assets/5182caf3-c775-4886-91d9-f0ddf51cb520" width="400" alt="Pytest"> | ✅ Available |
|  **Activity Log** | <img src="https://github.com/user-attachments/assets/88a3026f-8b26-4ea7-acb7-91953481cbfe" width="400" alt="Log"> | ✅ Available |

---

## 📄 License

This project is licensed under the **MIT License**. This means you are free to use, modify, and distribute this software for personal or educational purposes.

---

##  Author

<div align="center">
  <h3>pagarkristian</h3>
  <p>Cybersecurity Student • Python Learner • Open Source Enthusiast</p>
</div>
