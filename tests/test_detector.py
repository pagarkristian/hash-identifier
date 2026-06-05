from src.detector import identify_hash

def test_md5():
    result = identify_hash(
        "5f4dcc3b5aa765d61d8327deb882cf99"
    )
    assert result["name"] == "MD5"


def test_sha1():
    result = identify_hash(
        "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"
    )
    assert result["name"] == "SHA1"


def test_sha256():
    result = identify_hash(
        "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    )
    assert result["name"] == "SHA256"


def test_unknown():
    result = identify_hash(
        "abc123"
    )
    assert result["name"] == "Unknown"
