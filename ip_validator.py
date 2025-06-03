def is_valid_ip(ip_address):
    """Validate an IP address format (e.g., for DOCSIS gateway)."""
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

# Manual test
if __name__ == "__main__":
    print(is_valid_ip("192.168.1.1"))  # True
    print(is_valid_ip("256.1.2.3"))    # False
    print(is_valid_ip("1.2.3"))        # False