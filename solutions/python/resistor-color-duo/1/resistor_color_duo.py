def colors():
    return ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

def color_code(color):
    return colors().index(color)

def value(colors):
    out = ""
    for index in range(2):
        out += str(color_code(colors[index]))

    return int(out)