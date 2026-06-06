import os

from src.batch_scan import scan_file

def test_scan_file_valid(tmp_path):
    hash_file = tmp_path / "hashes.txt"
    hash_file.write_text(
        "5f4dcc3b5aa765d61d8327deb882cf99\n"
        "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d\n"
    )
    scan_file(str(hash_file))
    assert os.path.exists("reports/stats.json")

def test_scan_file_not_found():
    scan_file("nonexistent_file.txt")

def test_scan_file_empty(tmp_path):
    hash_file = tmp_path / "empty.txt"
    hash_file.write_text("")
    scan_file(str(hash_file))
