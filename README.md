# 🛡️ Hash Identifier

![Python Version](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Category](https://img.shields.io/badge/Field-Cybersecurity-red?style=for-the-badge)

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
      <td rowspan="7" align="center">⚙️ <br><b>Core Engine</b></td>
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
      <td rowspan="2" align="center">🔍 <br><b>Scanning Modes</b></td>
      <td>Single Hash Analysis</td>
      <td>Quick analysis for a single hash input via CLI.</td>
    </tr>
    <tr>
      <td>Batch Scanning</td>
      <td>Bulk processing by importing and parsing hashes from <code>.txt</code> files.</td>
    </tr>
    <tr>
      <td rowspan="3" align="center">📊 <br><b>Data & Output</b></td>
      <td>TXT Report</td>
      <td>Generates clean, human-readable text summaries for quick manual review.</td>
    </tr>
    <tr>
      <td>JSON Export</td>
      <td>Exports structured JSON data for easier processing and analysis..</td>
    </tr>
    <tr>
      <td>Activity Logging</td>
      <td>Records scan history and identified hash types..</td>
    </tr>
    <tr>
      <td rowspan="2" align="center">💻 <br><b>User Interface</b></td>
      <td>Interactive CLI Menu</td>
      <td>User-friendly, keyboard-navigable terminal menu.</td>
    </tr>
    <tr>
      <td>Colored Terminal Banner</td>
      <td>Styled with vibrant ANSI colors for a premium CLI look.</td>
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
│   ├── report.json
│   └── report.txt
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
│
├── README.md
└── LICENSE
```


---

## 🔍 Supported Algorithms

The tool uses precise cryptographic patterns to identify hashes based on their structural properties:

| Algorithm | Length (Chars) | Character Set | Format Example |
| :--- | :---: | :---: | :--- |
| `MD5` | **32** | Hexadecimal | `5f4dcc3b5aa765d61d8327deb882cf99` |
| `SHA-1` | **40** | Hexadecimal | `aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d` |
| `SHA-224` | **56** | Hexadecimal | `f2a52654a9b5fcf0cfdf6661a9fc553e1f13b6cb5561a293` |
| `SHA-256` | **64** | Hexadecimal | `2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824` |
| `SHA-384` | **96** | Hexadecimal | `59a17030e41e2f3d67bc8d48ef36b539cfdf62bbf6b553c5188ef7733f545` |
| `SHA-512` | **128** | Hexadecimal | `07e547d9586f6a73f73fbac0435ed76951218fb7d0c8d788a309d785436bbb64` |


---

## 🚀 Installation

Follow these steps to get the environment ready and run the tool on your local machine.

### Prerequisites
Make sure **Git** and **Python 3** are provisioned on your current deployment environment (e.g., Kali Linux, Parrot OS, or Ubuntu/WSL).

### Quick Start
Ensure Git and Python are provisioned on your deployment environment (Kali Linux, Parrot OS, etc.), then execute the following commands in your terminal:

```bash
# 1. Clone the repository
git clone [https://github.com/pagarkristian/hash-identifier.git](https://github.com/pagarkristian/hash-identifier.git)
```

```bash
# 2. Move into the project directory
cd hash-identifier
```

```bash
# 4.Launch the script directly by running:
python3 -m src.main
```

---

💡 Usage

🔹 1: Single Hash Verification

```Plaintext
Enter Hash: 5f4dcc3b5aa765d61d8327deb882cf99

[ Result ]
--------------------------------------------------
Hash Type   : MD5
Description : Message Digest Algorithm 5
Confidence  : Medium (Collisions Documented)
--------------------------------------------------
```


🔹 2: Batch Directory Processing
Terminal Operational Output Example:

```Plaintext
[1] MD5 (32 chars) -> Detected successfully
[2] SHA256 (64 chars) -> Detected successfully
[+] Scan compilation finalized. Reporting channels written to the 'reports/' directory.
```

---


## 📝 Reports

After each scan, the application generates reports inside: `reports/`

###  Output Examples

#### 1. Plaintext Report (`report.txt`)
```text
HASH IDENTIFIER REPORT
==================================================
Hash Value : 5f4dcc3b5aa765d61d8327deb882cf99
Hash Type  : MD5
Description: Message Digest Algorithm 5
Confidence : Medium
```

### 💡 JSON Report

`reports/report.json`

```json
{
  "hash_value": "5f4dcc3b5aa765d61d8327deb882cf99",
  "hash_type": "MD5",
  "description": "Message Digest Algorithm 5",
  "confidence": "Medium"
}
```

## 🪵 Logging

The application automatically saves your scan history so you can check your past work anytime. Everything is recorded in this file:

| File Name | Location | What it does |
| :--- | :--- | :--- |
| 📋 **Activity Log** | `logs/hash_identifier.log` | Saves the history of all the hashes you have scanned. |

---

### 📝 Example Log

Inside the log file, the data will look like this:

```text
[2026-06-04 21:15:30] HASH=5f4dcc3b5aa765d61d8327deb882cf99 TYPE=MD5
[2026-06-04 21:16:02] HASH=aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d TYPE=SHA-1
```

## 📊 Current Version

Here is the current status of the project and the features that are already working:

| Version | Status | Implemented Features |
| :---: | :---: | :--- |
| **v1.1** | ✅ Stable | • Hash Detection Engine<br>• Batch Scan Module<br>• TXT Report Export<br>• JSON Report Export<br>• Logging System<br>• Interactive Menu<br>• Colored Banner |

---

> 💡 **Note:** All features listed above are fully tested and ready to use. More updates and new features will be added in future versions!


## 🛣️ Project Roadmap

This is the plan for future updates and new features that will be added to the tool:

| Target Version | Status | Planned Features |
| :---: | :---: | :--- |
| **v1.2** | 🟡 Up Next | • Improved Statistics Module (Better data view)<br>• Better Error Handling (Fewer crashes)<br>• Enhanced Confidence Scoring<br>• Additional Unit Tests (Code testing) |
| **v2.0** | 🔵 Future | • Additional Hash Algorithms (More hash types)<br>• REST API Support<br>• Plugin-Based Architecture<br>• Advanced Classification System |

---

## 📸 Screenshots

Here are the visual previews of the tool in action:

| Preview Type | Screenshot | Status |
| :--- | :---: | :---: |
| 🖥️ **Main Menu Interface** | <img src="https://github.com/user-attachments/assets/66251afa-6cd9-4ec1-98eb-457c29ef5666" width="400" alt="Main Menu"> | ✅ Available |
| 🔍 **Batch Scanning Mode** | <img src="https://github.com/user-attachments/assets/23726e38-1661-4816-9998-f4692822143d" width="300" alt="Batch Scan 1"><br><br><img src="https://github.com/user-attachments/assets/989f92f2-408a-403f-b6e5-5893a24fde0a" width="300" alt="Batch Scan 2"> | ✅ Available |
| 📄 **Report Generation** | <img src="https://github.com/user-attachments/assets/fb9afdf6-4038-4b0c-9151-88b6db1f4fcd" width="400" alt="Report Output"> | ✅ Available |


---

## 📄 License

This project is licensed under the **MIT License**. This means you are free to use, modify, and distribute this software for personal or educational purposes.

---

## 👨‍💻 Author

<div align="center">
  <sub>Maintained by <b>pagarkristian</b>  helpful CLI tools with Python.</sub>
</div>

