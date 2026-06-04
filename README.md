# 🛡️ Hash Identifier

![Python Version](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Category](https://img.shields.io/badge/Field-Cybersecurity-red?style=for-the-badge)

**Hash Identifier** is a Python-based Command Line Interface (CLI) tool designed to identify common cryptographic hash algorithms using pattern matching and length validation.

This project was developed as a cybersecurity learning project to help students, CTF participants, and security enthusiasts quickly classify unknown hash values.

---

## 🚀 Features

Here is a detailed breakdown of the capabilities and features included in this tool:

| Category | Feature | Description |
| :--- | :--- | :--- |
| 🔍 **Hash Detection** | MD5 | Accurately identifies 128-bit MD5 hashes. |
| | SHA-1 | Detects 160-bit SHA-1 cryptographic hashes. |
| | SHA-224 / SHA-256 | Validates and identifies SHA-2 family (224 and 256-bit). |
| | SHA-384 / SHA-512 | Supports high-security SHA-2 family (384 and 512-bit). |
| ⚙️ **Scanning Modes** | Single Hash Analysis | Quick analysis for a single hash input. |
| | Batch Hash Scanning | Bulk scan hashes directly from uploaded `.txt` files. |
| 📊 **Reporting** | TXT Report | Generates clean, human-readable text reports. |
| | JSON Report | Exports structured data perfect for integration with other tools. |
| 🪵 **Monitoring** | Activity Logging | Keeps track of all scan activities and timestamps. |
| 💻 **User Interface** | Interactive Terminal Menu | User-friendly, keyboard-navigable CLI menu. |
| | Colored CLI Banner | Styled with vibrant ANSI colors for a premium look. |

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




## 📊 Supported Algorithms

| Cryptographic Hash | Digest Length | Character Class | Confidence Unit |
| :--- | :---: | :---: | :--- |
| **MD5** | `32 Chars` | Hexadecimal (`a-f, 0-9`) | ⚠️ Medium *(High collision potential)* |
| **SHA-1** | `40 Chars` | Hexadecimal (`a-f, 0-9`) | ✅ High |
| **SHA-224** | `56 Chars` | Hexadecimal (`a-f, 0-9`) | ✅ High |
| **SHA-256** | `64 Chars` | Hexadecimal (`a-f, 0-9`) | ✅ High |
| **SHA-384** | `96 Chars` | Hexadecimal (`a-f, 0-9`) | ✅ High |
| **SHA-512** | `128 Chars` | Hexadecimal (`a-f, 0-9`) | ✅ High |



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
# 3. Launch the tool
python3 hash_identifier.py
```

```bash
# 4.Launch the script directly by running:
python3 -m src.main
```


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
