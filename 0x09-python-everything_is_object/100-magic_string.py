def magic_string():
    if not hasattr(magic_string, 'count'):
        magic_string.count = 1
    else:
        magic_string.count += 1

    return "BestSchool, " * (magic_string.count - 1) + "BestSchool"
