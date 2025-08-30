def is_valid_ip(ip_address):
    """Validate an IP address format."""
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

def test_ip_validator():
    assert is_valid_ip("192.168.2.1") == True, "Valid IP failed"
    assert is_valid_ip("256.1.2.3") == False, "Invalid IP (out of range) failed"
    assert is_valid_ip("1.2.3") == False, "Invalid IP (wrong format) failed"