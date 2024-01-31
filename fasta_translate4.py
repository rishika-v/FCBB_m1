import sys
from fasta_translate1 import read_fasta

def read_codon(file):
    codon_table = {}
    with open(file, 'r') as f:
        for line in f:
            vals = line.strip().split()
            amino = vals[1]
            codons = vals[2].split(',')
            for codon in codons:
                codon_table[codon] = amino
    return codon_table

def translate_dna(seq, codon_table):
    protein = []
    for i in range (0, len(seq), 3):
        codon = seq[i:i+3].upper()
        if codon in codon_table:
            amino = codon_table[codon]
            if amino == "*":
                break
            protein.append(amino)
        else:
            print(f"Error: invalid nucleotide in codon: {codon}")
    return ''.join(protein)

codon_table = read_codon('codon_table_hard.txt')
fasta = read_fasta()

for id, seq in fasta.items():
    protein_seq = translate_dna(seq, codon_table)
    print(f">{id}")
    print(protein_seq)
