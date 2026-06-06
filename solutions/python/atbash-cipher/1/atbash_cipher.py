def encode(plain_text):
    cleaned_chars = [char.lower() for char in plain_text if char.isalnum()]
    
    ciphered_chars = []
    for char in cleaned_chars:
        if char.isalpha():
            ciphered_chars.append(chr(219 - ord(char)))
        else:
            ciphered_chars.append(char)
            
    cipher_string = "".join(ciphered_chars)
    return " ".join(cipher_string[i:i+5] for i in range(0, len(cipher_string), 5))


def decode(ciphered_text):
    cleaned_chars = [char.lower() for char in ciphered_text if char.isalnum()]

    plain_chars = []
    for char in cleaned_chars:
        if char.isalpha():
            plain_chars.append(chr(219 - ord(char)))
        else:
            plain_chars.append(char)

    return "".join(plain_chars)