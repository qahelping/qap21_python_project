def custom_sum(arg=None):
    if arg:
        total = 0
        for val in arg:
            if isinstance(val, (int, float)):
                total += val
        return round(total, 2)
    return 0
