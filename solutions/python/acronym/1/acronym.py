def abbreviate(words):
    output = words[0].upper()

    after_ws = False

    for char in words:
        if after_ws and char.isalpha():
            output += char.upper()
            after_ws = False
            continue
        if char.isspace() or char == "-":
            after_ws = True

    return output
