def map_value(min, max, value, new_min, new_max):
    range = max - min
    new_range = new_max - new_min
    return (((value - min) * new_range) / range) + new_min