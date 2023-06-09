# The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

# The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

# Given: An RNA string s

# corresponding to a strand of mRNA (of length at most 10 kbp).

# Return: The protein string encoded by s.

input_RNA = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

codon_to_amino_dict = {
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGU": "C",
    "UGC": "C",
    "UGA": "STOP",
    "UGG": "W",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G"
} 

output_str = ""

def RNA_to_amino(codon: str, compare_dict: dict):
    return compare_dict[f"{codon}"]

def RNA_to_protein(RNA: str,output: str):
    if len(RNA) % 3 != 0:
        return None
    if len(RNA) != 0:
        codon, rest = RNA[:3], RNA[3:] 
        output += RNA_to_amino(codon,codon_to_amino_dict)
        RNA_to_protein(rest,output)
    return output

RNA_to_protein(input_RNA,output_str)
print(output_str)