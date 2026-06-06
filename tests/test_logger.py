import os

from src.logger import write_log

def test_write_log_creates_file():
    write_log(
        "5f4dcc3b5aa765d61d8327deb882cf99",
        "MD5"
    )
    assert os.path.exists("logs/hash_identifier.log")

def test_write_log_contains_hash():
    write_log(
        "5f4dcc3b5aa765d61d8327deb882cf99",
        "MD5"
    )
    with open("logs/hash_identifier.log", "r") as f:
        content = f.read()
    assert "5f4dcc3b5aa765d61d8327deb882cf99" in content

def test_write_log_contains_type():
    write_log(
        "5f4dcc3b5aa765d61d8327deb882cf99",
        "MD5"
    )
    with open("logs/hash_identifier.log", "r") as f:
        content = f.read()
    assert "TYPE=MD5" in content
