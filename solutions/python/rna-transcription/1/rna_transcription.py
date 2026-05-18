def to_rna(dna_strand):
    out = ""
    for char in dna_strand:
        if char == "G":
            out += "C"
        if char == "C":
            out += "G"
        if char == "T":
            out += "A"
        if char == "A":
            out += "U"
    return out
