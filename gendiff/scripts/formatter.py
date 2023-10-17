def stringify(value):
    if isinstance(value, bool):
        if value:
            return 'true'
        else:
            return 'false'
    return value
