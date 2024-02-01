import sys

def read_fasta():
    fasta_dict = {}
    sequence_id = None
    sequence_data = []
    for line in sys.stdin:
        line = line.strip()
        if line.startswith(">"):
            if sequence_id:
                fasta_dict[sequence_id] = ''.join(sequence_data)
                sequence_data = []
            sequence_id = line[1:]
        else:
            sequence_data.append(line)
    if sequence_id:
        fasta_dict[sequence_id] = ''.join(sequence_data)
    return fasta_dict

def read_codon(file):
    codon_table = {}
    with open(file, 'r') as f:
        for line in f:
            vals = line.strip().split()
            if len(vals) == 2:
                codon, amino = vals
                codon_table[codon] = amino
    return codon_table

def translate_dna(seq, codon_table):
    protein = []
    for i in range (0, len(seq), 3):
        codon = seq[i:i+3].upper()
        if codon in codon_table:
            amino = codon_table[codon]
            protein.append(amino)
    return ''.join(protein)

codon_table = read_codon('codon_table.txt')
fasta = read_fasta()

id_list = list(fasta.keys())
id = id_list[0]
seq = fasta.get(id)
protein_seq = translate_dna(seq, codon_table)
print(f">{id}", file=sys.stdout)
print(protein_seq, file=sys.stdout)
