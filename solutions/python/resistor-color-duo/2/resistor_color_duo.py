def color_list():
    return ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

def color_code(color):
    return color_list().index(color)

def value(colors):
    out = ""
    for index in range(2):
        out += str(color_code(colors[index]))

    return int(out)