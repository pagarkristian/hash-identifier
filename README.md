# Hash Identifier

Cybersecurity learning project for identifying hash algorithms using Python.

## Features

* Detect MD5
* Detect SHA1
* Detect SHA224
* Detect SHA256
* Detect SHA384
* Detect SHA512
* Generate TXT reports
* Generate JSON reports
* Store scan logs
* Display scan statistics
* Support batch scanning from file

## Project Structure

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
│   ├── report.txt
│   └── report.json
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
├── README.md
└── LICENSE
```

## Supported Hashes

| Hash Type | Length |
| --------- | ------ |
| MD5       | 32     |
| SHA1      | 40     |
| SHA224    | 56     |
| SHA256    | 64     |
| SHA384    | 96     |
| SHA512    | 128    |

## Installation

Clone repository:

```bash
git clone https://github.com/pagarkristian/hash-identifier.git
cd hash-identifier
```

Run:

```bash
python3 -m src.main
```

## Usage

### Single Hash Scan

```text
1. Single Hash Scan
2. Batch Scan From File
```

Example:

```text
Enter Hash:
5f4dcc3b5aa765d61d8327deb882cf99
```

Output:

```text
Hash Type: MD5
Description: Message Digest Algorithm 5
Confidence: Medium
```

### Batch Scan

File:

```text
examples/hashes.txt
```

Example:

```text
5f4dcc3b5aa765d61d8327deb882cf99
55ab0f70a169b59663da671f5581298491bbec81640fa889241517a6c6ec22fc
```

Output:

```text
[1] MD5 (32 chars)
[2] SHA256 (64 chars)
```

## Reports

TXT Report:

```text
reports/report.txt
```

JSON Report:

```text
reports/report.json
```

## Logs

Scan activity is stored in:

```text
logs/hash_identifier.log
```

## Statistics

Display scan statistics using the statistics module.

## Roadmap

### Version 1.1

* JSON Report Export
* Batch Hash Scan
* Interactive Menu

### Version 1.2

* Color Output
* Confidence Score
* Better Statistics

### Version 2.0

* API Mode
* Advanced Classification
* Multi Report Formats

## License

MIT License
