# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

import re

input = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""
def GCcontent(seq: str):
    g_count = seq.count("G")
    c_count = seq.count("C")
    return  (g_count + c_count) / len(seq) * 100

def compareGC(db_entry):
    
    biggest_gc = db_entry[0]["gc_content"]
    biggest_gc_index = 0

    for i in  range(0,len(db_entry)):
        if db_entry[i]["gc_content"] > biggest_gc:
            biggest_gc = db_entry[i]["gc_content"]
            biggest_gc_index = i
    return db_entry[biggest_gc_index]

ids = re.findall(r'Rosalind_\d+',input)
dnaSeqString = re.split(r'>Rosalind_\d+',input)
dnaSeq = []
for i in dnaSeqString:
    dnaSeq.append(re.sub("\n", "", i))
dnaSeq.pop(0)

output = []

for i in range(0,len(ids)):
    output.append({
        "id": ids[i],
        "seq": dnaSeq[i],
        "gc_content": GCcontent(dnaSeq[i])
    })

print(compareGC(output)["id"])
print(compareGC(output)["gc_content"])


