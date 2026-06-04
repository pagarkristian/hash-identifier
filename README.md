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
      <th>Category</th>
      <th>Feature</th>
      <th>Capabilities</th>
    </tr>
  </thead>
  <tbody>
    <!-- HASH DETECTION -->
    <tr>
      <td rowspan="4" align="center">🕵️‍♂️ <br><b>Hash Detection</b></td>
      <td><code>MD5</code></td>
      <td>Identifies standard 128-bit MD5 hashes.</td>
    </tr>
    <tr>
      <td><code>SHA-1</code></td>
      <td>Detects 160-bit SHA-1 cryptographic hashes.</td>
    </tr>
    <tr>
      <td><code>SHA-224 / SHA-256</code></td>
      <td>Validates SHA-2 family (224 and 256-bit) hashes.</td>
    </tr>
    <tr>
      <td><code>SHA-384 / SHA-512</code></td>
      <td>Supports high-security SHA-2 family (384 and 512-bit).</td>
    </tr>
    <!-- SCANNING MODES -->
    <tr>
      <td rowspan="2" align="center">⚙️ <br><b>Scanning Modes</b></td>
      <td>Single Analysis</td>
      <td>Quick analysis for a single hash input via CLI.</td>
    </tr>
    <tr>
      <td>Batch Scanning</td>
      <td>Bulk processing by importing hashes from <code>.txt</code> files.</td>
    </tr>
    <!-- REPORTING & LOGS -->
    <tr>
      <td rowspan="3" align="center">📊 <br><b>Data & Output</b></td>
      <td>TXT Report</td>
      <td>Generates clean, human-readable text summaries.</td>
    </tr>
    <tr>
      <td>JSON Export</td>
      <td>Exports structured data for automation or API integration.</td>
    </tr>
    <tr>
      <td>Activity Logging</td>
      <td>Keeps track of all execution steps and scan history.</td>
    </tr>
    <!-- UI/UX -->
    <tr>
      <td rowspan="2" align="center">💻 <br><b>User Interface</b></td>
      <td>Interactive Menu</td>
      <td>User-friendly, keyboard-navigable terminal menu.</td>
    </tr>
    <tr>
      <td>Colored CLI Banner</td>
      <td>Styled with vibrant ANSI colors for a premium terminal look.</td>
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

## 📝 Reports & Output

The tool automatically organizes and saves scan results into dedicated formats inside the `reports/` directory:
```html
<table>
  <thead>
    <tr>
      <th width="30%">Report Type</th>
      <th width="40%">Default Output Path</th>
      <th width="30%">Primary Use Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>📄 <b>TXT Report</b></td>
      <td><code>reports/report.txt</code></td>
      <td>Human-readable summary for quick manual reviews.</td>
    </tr>
    <tr>
      <td>📊 <b>JSON Report</b></td>
      <td><code>reports/report.json</code></td>
      <td>Structured data for automation, logging, or API parsing.</td>
    </tr>
  </tbody>
</table>

### 💡 Example JSON Output

When exporting to JSON, the data structure is strictly formatted as follows, making it easy to pipe into other penetration testing frameworks or custom scripts:

```json
{
  "hash_value": "5f4dcc3b5aa765d61d8327deb882cf99",
  "hash_type": "MD5",
  "description": "Message Digest Algorithm 5",
  "confidence": "Medium"
}
```
