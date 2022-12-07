myPath = "C:/Users/Coulo/Desktop/Biopython/"
import os.path
from os import path

# Working with sequence
import Bio
print(Bio.__version__)

from Bio.Seq import Seq
#from Bio.Alphabet import generic_dna

my_dna = Seq("AGTACACTGGT") #, generic_dna)
print(my_dna)
print(my_dna.complement())
print(my_dna.reverse_complement())
print(my_dna.transcribe())


# Reading Sequence Files in Biopython
# compte le nb de lignes
from Bio import SeqIO
#help(SeqIO)

filename = myPath + "NC_000913.faa"
count = 0
for record in SeqIO.parse(filename, "fasta"):
    count = count + 1
print("There were " + str(count) + " records in file " + filename)

# compte record
from Bio import SeqIO
filename = myPath + "NC_000913.faa"
for record in SeqIO.parse(filename, "fasta"):
    print("Record " + record.id + ", length " + str(len(record.seq)))

# Checking proteins start with methionine
from Bio import SeqIO
filename = myPath + "NC_000913.faa"
bad = 0
for record in SeqIO.parse(filename, "fasta"):
    if not record.seq.startswith("M"):
        bad = bad + 1
        print(record.id + " starts " + record.seq[0])
print("Found " + str(bad) + " records in " + filename + " which did not start with M")

# deuxieme fichier qui renvoie erreur
from Bio import SeqIO
filename = myPath + "PGSC_DM_v3.4_pep_representative.fasta"
bad = 0
for record in SeqIO.parse(filename, "fasta"):
    if not record.seq.startswith("M"):
        bad = bad + 1
        print(record.id + " starts " + record.seq[0])
print("Found " + str(bad) + " records in " + filename + " which did not start with M")

# Converting a sequence file

from Bio import SeqIO
input_filename = myPath + "NC_000913.gbk"
output_filename = myPath + "NC_000913_converted.fasta"
count = SeqIO.convert(input_filename, "gb", output_filename, "fasta")
print(str(count) + " records converted")

# Filtering a sequence file
from Bio import SeqIO
input_filename = myPath + "NC_000913.faa"
output_filename = myPath + "NC_000913_long_only.faa"
count = 0
total = 0
output_handle = open(output_filename, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    total = total + 1
    if 100 <= len(record):
        count = count + 1
        SeqIO.write(record, output_handle, "fasta")
output_handle.close()
print(str(count) + " records selected out of " + str(total))

# Editing sequences
from Bio import SeqIO
input_filename = myPath + "PGSC_DM_v3.4_pep_representative.fasta"
output_filename =  myPath + "PGSC_DM_v3.4_pep_rep_no_stars.fasta"
output_handle = open(output_filename, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    cut_record = record[:-1] # remove last letter
    #print(cut_record)
    SeqIO.write(cut_record, output_handle, "fasta")
output_handle.close()

# Working with Sequence Features
from Bio import SeqIO
record = SeqIO.read(myPath + "NC_000913.gbk", "genbank")
output_handle = open(myPath + "NC_000913_cds.fasta", "w")
count = 0
for feature in record.features:
    if feature.type == "CDS":
        count = count + 1
        feature_name = "locus_tag" # Use feature.qualifiers or feature.dbxrefs here
        feature_seq = feature.extract(record.seq)
        # Simple FASTA output without line wrapping:
        output_handle.write(">" + feature_name + "\n" + str(feature_seq) + "\n")
output_handle.close()
print(f"{count} CDS sequences extracted")

# loops over all the features looking for gene records, and calculates their total length
from Bio import SeqIO
record = SeqIO.read(myPath  + "NC_000913.gbk", "genbank")
total = 0
for feature in record.features:
    if feature.type == "gene":
        total = total + len(feature)
print("Total length of all genes is " + str(total))


# Phylogenetics with Bio.Phylo
from Bio import Phylo
tree = Phylo.read(myPath + "simple.dnd", "newick")
print(tree)

# afficher un arbre dans le terminal
from Bio import Phylo
tree = Phylo.read(myPath + "simple.dnd", "newick")
Phylo.draw_ascii(tree)

#afficher arbre avec matplolib
from Bio import Phylo
tree = Phylo.read(myPath + "simple.dnd", "newick")
tree.rooted = True
Phylo.draw(tree)

# Filtering a sequence file ERROR
# from Bio import SeqIO
# input_filename = myPath + "NC_000913.faa"
# output_filename = myPath + "NC_000913_long_only.faa"
# count = 0
# total = 0
# for record in SeqIO.parse(input_filename, "fasta"):
#     total = total + 1
#     if 100 <= len(record):
#         count = count + 1
#         SeqIO.write(record, output_handle, "fasta")
# print(str(count) + " records selected out of " + str(total))

# selection records
from Bio import SeqIO
input_filename = myPath + "NC_000913.faa"
output_filename = myPath + "NC_000913_long_only.faa"
count = 0
total = 0
output_handle = open(output_filename, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    total = total + 1
    if 100 <= len(record):
        count = count + 1
        SeqIO.write(record, output_handle, "fasta")
output_handle.close()
print(str(count) + " records selected out of " + str(total))

# Editing sequences
from Bio import SeqIO
input_filename = myPath + "PGSC_DM_v3.4_pep_representative.fasta"
output_filename = myPath + "PGSC_DM_v3.4_pep_rep_no_stars.fasta"
output_handle = open(output_filename, "w")
for record in SeqIO.parse(input_filename, "fasta"):
    cut_record = record[:-1] # remove last letter
    SeqIO.write(cut_record, output_handle, "fasta")
output_handle.close()

# Working with Sequence Features
from Bio import SeqIO
record = SeqIO.read(myPath + "NC_000913.gbk", "genbank")
output_handle = open(myPath + "NC_000913_cds.fasta", "w")
count = 0
for feature in record.features:
    if feature.type == "CDS":
        count = count + 1
        feature_name = "locus_tag" # Use feature.qualifiers or feature.dbxrefs here
        feature_seq = feature.extract(record.seq)
        # Simple FASTA output without line wrapping:
        output_handle.write(">" + feature_name + "\n" + str(feature_seq) + "\n")
output_handle.close()
print(str(count) + " CDS sequences extracted")

# loops over all the features looking for gene records, and calculates their total length
from Bio import SeqIO
record = SeqIO.read(myPath + "NC_000913.gbk", "genbank")
total = 0
for feature in record.features:
    if feature.type == "gene":
        total = total + len(feature)
print("Total length of all genes is " + str(total))


from Bio import Phylo
tree = Phylo.read(myPath + "simple.dnd", "newick")
print(tree)

from Bio import Phylo
tree = Phylo.read(myPath + "simple.dnd", "newick")
Phylo.draw_ascii(tree)

from Bio import Phylo
tree = Phylo.read(myPath + "simple.dnd", "newick")
tree.rooted = True
