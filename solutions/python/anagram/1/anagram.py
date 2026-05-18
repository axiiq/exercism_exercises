def find_anagrams(word, candidates):
    anagrams = []

    letters = {}
    word_len = len(word)

    for char in set(word):
        letters[char.lower()] = word.count(char)

    for candidate in candidates:
        if candidate.lower() == word.lower(): continue
        if len(candidate) != word_len: continue
        
        selected = candidate.lower()
        helper_counter = 0
        for key, value in letters.items():
            if selected.count(key) != value: break
            helper_counter += value

            if helper_counter == word_len:
                anagrams.append(candidate)

    return anagrams
    