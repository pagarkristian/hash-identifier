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

def test_sha224():
    result = identify_hash(
        "ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193"
    )
    assert result["name"] == "SHA224"

def test_sha256():
    result = identify_hash(
        "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    )
    assert result["name"] == "SHA256"

def test_sha384():
    result = identify_hash(
        "59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f"
    )
    assert result["name"] == "SHA384"

def test_sha512():
    result = identify_hash(
        "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043"
    )
    assert result["name"] == "SHA512"

def test_unknown():
    result = identify_hash(
        "abc123"
    )
    assert result["name"] == "Unknown"

def test_empty_string():
    result = identify_hash(
        ""
    )
    assert result["name"] == "Unknown"

def test_whitespace_stripped():
    result = identify_hash(
        "  5f4dcc3b5aa765d61d8327deb882cf99  "
    )
    assert result["name"] == "MD5"
