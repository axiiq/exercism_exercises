def proteins(strand):
    codons = []
    codon_table = {"AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine",  "UCC": "Serine",  "UCA": "Serine", "UCG": "Serine", "UAU": "Tyrosine",  "UAC": "Tyrosine", "UGU": "Cysteine",  "UGC": "Cysteine", "UGG": "Tryptophan"}
    
    for index in range(len(strand)):
        if index % 3 != 0: continue
        cod_seq = strand[index:index+3]
        if cod_seq == "UAA" or cod_seq == "UAG" or cod_seq == "UGA": break
        codons.append(cod_seq)

    output = []
    for codon in codons:
        output.append(codon_table[codon])

    return output