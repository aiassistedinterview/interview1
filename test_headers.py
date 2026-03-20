from headers import normalize_headers

def test_duplicate_headers_preserve_first():
    headers = {
        "Content-Type": "application/json",
        "content-type": "text/plain"
    }

    result = normalize_headers(headers)
    assert result["content-type"] == "application/json"