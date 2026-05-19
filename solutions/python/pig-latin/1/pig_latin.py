import re

def translate_word(word):
    if re.match(r'^([aeiou]|xr|yt)', word):
        return word + "ay"

    match_qu = re.match(r'^([^aeiou]*qu)(.*)', word)
    if match_qu:
        return match_qu.group(2) + match_qu.group(1) + "ay"

    match_y = re.match(r'^([^aeiou]+)(y.*)', word)
    if match_y:
        return match_y.group(2) + match_y.group(1) + "ay"
        
    match_consonants = re.match(r'^([^aeiou]+)(.*)', word)
    if match_consonants:
        return match_consonants.group(2) + match_consonants.group(1) + "ay"

    return word


def translate(text):
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return " ".join(translated_words)