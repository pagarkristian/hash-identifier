# 🛡️ Hash Identifier

![Python Version](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Category](https://img.shields.io/badge/Field-Cybersecurity-red?style=for-the-badge)

**Hash Identifier** is a lightweight, modular, and high-performance Command Line Interface (CLI) utility built in Python. It evaluates, matches, and classifies cryptographic signatures or hashes based on strict character digests, exact lengths, and structural pattern boundaries. 

This project serves as an essential initial triage instrument for digital forensics examiners, incident responders, and security analysts looking to identify unknown hashes during malware analysis or data auditing.

---

## ✨ Key Features

* 🔍 **Multi-Algorithm Signatures**: High-precision recognition for MD5, SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512.
* 📂 **Automated Batch Processing**: Efficiently ingests, cleans, and processes bulk hash lists from a single flat text (`.txt`) file.
* 🎨 **Polished UX/UI Design**: Features an interactive terminal experience utilizing ANSI color escape sequences and an aligned telemetry header.
* 📊 **Telemetry & Runtime Statistics**: Aggregates comprehensive success rates, breakdown percentages, and target metrics instantly post-scan.
* 📝 **Dual-Engine Reporting Module**: Automatically isolates and exports runtime outputs into human-readable raw text summaries and machine-parsable JSON structures.
* 🪵 **Immutable Security Auditing**: Tracks all logical transitions and application lifecycles inside dedicated background rotation logs for historical compliance.

---

## 📂 Project Structure

```text
hash-identifier/
│
├── examples/
│   └── hashes.txt             # Target input sample containing bulk hash signatures
│
├── logs/
│   └── hash_identifier.log    # Persistent runtime logs for application auditing
│
├── reports/
│   ├── report.json            # Machine-readable scan output structured in JSON
│   └── report.txt             # Well-formatted standalone text report
│
├── src/
│   ├── __init__.py
│   ├── banner.py              # Manages cross-platform screen clearing and CLI aesthetics
│   ├── batch_scan.py          # Core workflow handling file streaming and bulk validation
│   ├── detector.py            # Primary regex engine for signature validation
│   ├── logger.py              # Logging engine infrastructure setup
│   ├── main.py                # Central orchestrator and entry-point of the program
│   ├── patterns.py            # Hardcoded cryptographic validation models
│   ├── report.py              # Export handlers for file writing sub-modules
│   └── stats.py               # Calculation matrix engine for telemetry reporting
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



## 🚀 Installation & Setup

Follow these steps to get the environment ready and run the tool on your local machine.

### Prerequisites
Make sure **Git** and **Python 3** are provisioned on your current deployment environment (e.g., Kali Linux, Parrot OS, or Ubuntu/WSL).

### Quick Start

```markdown
## 🚀 Installation & Setup
```
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


💡 Usage Demonstrations
🔹 Scenario A: Single Hash Verification
Provide a single arbitrary hash string to the CLI evaluation parameter block:


```Plaintext
Enter Hash: [1;32m5f4dcc3b5aa765d61d8327deb882cf99[0m

[1;34m[ Result ][0m
--------------------------------------------------
[1mHash Type   :[0m MD5
[1mDescription :[0m Message Digest Algorithm 5
[1mConfidence  :[0m Medium (Collisions Documented)
--------------------------------------------------
```


🔹 Scenario B: Batch Directory Processing
Populate your collection of multi-signature lists into examples/hashes.txt (one signature per line), and trigger Option 2 on the interactive application panel.

Terminal Operational Output Example:

```Plaintext
[1;36m[1][0m MD5 (32 chars) -> [1;32mDetected successfully[0m
[1;36m[2][0m SHA256 (64 chars) -> [1;32mDetected successfully[0m
[1;34m[+][0m Scan compilation finalized. Reporting channels written to the [1m'reports/'[0m directory.
```
