def resistor_label(colors):
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    
    tolerance_dict = {
        "grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
        "brown": 1, "red": 2, "gold": 5, "silver": 10
    }

    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    has_tolerance = colors[-1] in tolerance_dict
    value_colors = colors[:-1] if has_tolerance else colors
    
    digits = ""
    for color in value_colors[:-1]:
        digits += str(color_list.index(color))
    
    multiplier = color_list.index(value_colors[-1])
    
    ohms = int(digits) * (10 ** multiplier)

    if ohms >= 1_000_000_000:
        value = ohms / 1_000_000_000
        unit = "gigaohms"
    elif ohms >= 1_000_000:
        value = ohms / 1_000_000
        unit = "megaohms"
    elif ohms >= 1_000:
        value = ohms / 1_000
        unit = "kiloohms"
    else:
        value = ohms
        unit = "ohms"

    if value == int(value):
        value = int(value)

    label_text = f"{value} {unit}"
    if has_tolerance:
        tolerance = tolerance_dict[colors[-1]]
        label_text += f" ±{tolerance}%"

    return label_text