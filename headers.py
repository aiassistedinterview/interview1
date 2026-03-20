def normalize_headers(headers: dict) -> dict:
    """
    Normalize HTTP headers so lookups are case-insensitive.
    """
    normalized = {}
    for key, value in headers.items():
        normalized[key.lower()] = value
    return normalized
