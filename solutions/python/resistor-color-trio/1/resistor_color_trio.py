def color_list():
    return ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

def color_code(color):
    return color_list().index(color)

def value(colors):
    out = ""
    for index in range(2):
        out += str(color_code(colors[index]))
    zero_count = color_code(colors[2])

    out += "0" * zero_count
    
    return int(out)

def label(colors):
    ohms = value(colors)
    label_text = ""

    if ohms == 0:
        return "0 ohms"

    if ohms % 1_000_000_000 == 0:
        label_text += str(int(ohms / 1_000_000_000))
        label_text += " giga"
    elif ohms % 1_000_000 == 0:
        label_text += str(int(ohms / 1_000_000))
        label_text += " mega"
    elif ohms % 1_000 == 0:
        label_text += str(int(ohms / 1_000))
        label_text += " kilo"
    else:
        label_text += str(ohms)
        label_text += " "

    label_text += "ohms"
    
    return label_text
