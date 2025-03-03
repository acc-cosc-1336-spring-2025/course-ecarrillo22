#
def get_hamming_distance(dna1, dna2):

    hamming_distance = 0
    
    for nucleotide in range(len(dna1)):
        if dna1[nucleotide] != dna2[nucleotide]:
            hamming_distance += 1
            
    return hamming_distance


#def get_dna_complement(dna):