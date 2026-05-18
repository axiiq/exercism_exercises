DATA = [
    ("house that Jack built.", ""),
    ("malt", "that lay in the "),
    ("rat", "that ate the "),
    ("cat", "that killed the "),
    ("dog", "that worried the "),
    ("cow with the crumpled horn", "that tossed the "),
    ("maiden all forlorn", "that milked the "),
    ("man all tattered and torn", "that kissed the "),
    ("priest all shaven and shorn", "that married the "),
    ("rooster that crowed in the morn", "that woke the "),
    ("farmer sowing his corn", "that kept the "),
    ("horse and the hound and the horn", "that belonged to the ")
    ]
    
def get_verse(number):
    idx = number - 1
    
    verse_parts = [f"This is the {DATA[idx][0]}"]
    
    for i in range(idx, 0, -1):
        action = DATA[i][1]
        previous_subject = DATA[i-1][0]
        
        verse_parts.append(f"{action}{previous_subject}")
        
    return " ".join(verse_parts)

def recite(start_verse, end_verse):
    verses = []
    for i in range(start_verse, end_verse + 1):
        verses.append(get_verse(i))
    return verses