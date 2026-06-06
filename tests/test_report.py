import os
import json

from src.report import save_report

def test_save_report_txt():
    result = {
        "name": "MD5",
        "description": "Message Digest Algorithm 5 ",
        "confidence": "High"
    }
    save_report(
        "5f4dcc3b5aa765d61d8327deb882cf99",
        result
    )
    assert os.path.exists("reports/report.txt")

def test_save_report_json():
    result = {
        "name": "MD5",
        "description": "Message Digest Algorithm 5 ",
        "confidence": "High"
    }
    save_report(
        "5f4dcc3b5aa765d61d8327deb882cf99",
        result
    )
    with open("reports/report.json", "r") as f:
        data = json.load(f)
    assert data["hash_type"] == "MD5"

def test_save_report_has_timestamp():
    result = {
        "name": "MD5",
        "description": "Message Digest Algorithm 5 ",
        "confidence": "High"
    }
    save_report(
        "5f4dcc3b5aa765d61d8327deb882cf99",
        result
    )
    with open("reports/report.json", "r") as f:
        data = json.load(f)
    assert "timestamp" in data

def test_save_report_has_hash_length():
    result = {
        "name": "MD5",
        "description": "Message Digest Algorithm 5 ",
        "confidence": "High"
    }
    save_report(
        "5f4dcc3b5aa765d61d8327deb882cf99",
        result
    )
    with open("reports/report.json", "r") as f:
        data = json.load(f)
    assert data["hash_length"] == 32

def test_save_report_confidence_high():
    result = {
        "name": "MD5",
        "description": "Message Digest Algorithm 5 ",
        "confidence": "High"
    }
    save_report(
        "5f4dcc3b5aa765d61d8327deb882cf99",
        result
    )
    with open("reports/report.json", "r") as f:
        data = json.load(f)
    assert data["confidence"] == "High"

def test_save_report_returns_path():
    result = {
        "name": "SHA256",
        "description": "Secure Hash Algorithm 256 ",
        "confidence": "Medium"
    }
    path = save_report(
        "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
        result
    )
    assert path == "reports/report.txt"
