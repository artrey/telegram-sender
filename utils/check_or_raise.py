def check_or_raise(value, error_type):
    if not value:
        raise error_type()
    return value
