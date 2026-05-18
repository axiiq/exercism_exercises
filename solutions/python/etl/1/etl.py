def transform(legacy_data):
    new_dict = {}

    for key, value in legacy_data.items():
        for char in value:
            new_dict[char.lower()] = key
            
    return new_dict
