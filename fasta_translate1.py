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

fasta = read_fasta()
print(fasta, file=sys.stdout)
