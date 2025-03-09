#
def get_hamming_distance(dna1, dna2):

    hamming_distance = 0
    
    for nucleotide in range(len(dna1)):
        if dna1[nucleotide] != dna2[nucleotide]:
            hamming_distance += 1
            
    return hamming_distance


def get_dna_complement(dna):

    new_dna = ''

    for nucleotide in dna:
                
        if nucleotide == 'A':
            new_dna += 'T'
        elif nucleotide == 'T':
            new_dna += 'A'
        elif nucleotide == 'C':
            new_dna += 'G'
        elif nucleotide == 'G':
            new_dna += 'C'
        
    reverse_dna = new_dna[::-1]

    return reverse_dna

def valid_dna(dna):
    
    for nuc in dna:
        if nuc not in "AGCT":
            return False
    
    return True

    
