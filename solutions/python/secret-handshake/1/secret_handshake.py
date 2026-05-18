def commands(binary_str):
    actions = []
    num = int(binary_str, 2)

    if num & 0b00001 == 0b00001:
        actions.append("wink")

    if num & 0b00010 == 0b00010:
        actions.append("double blink")

    if num & 0b00100 == 0b00100:
        actions.append("close your eyes")

    if num & 0b01000 == 0b01000:
        actions.append("jump")

    if num & 0b10000 == 0b10000:
        actions = actions[::-1]

    return actions