import sys
from Bio import Entrez, SeqIO

usage = 'Usage: ' + sys.argv[0] + ' email Genus species gene '

if len(sys.argv) != 5:
    print(usage)
    exit()

email = sys.argv[1]
genus = sys.argv[2]
species = sys.argv[3]
gene = sys.argv[4]

Entrez.email = "%s" % (email)

handle = Entrez.esearch(db="nucleotide", term='%s AND "%s %s"[Organism]' % (gene, genus, species))
rec_list = Entrez.read(handle)
handle.close()

nbrecords = len(rec_list['IdList'])
print('the ncbi nucleotide database had', nbrecords, 'sequences corresponding to your request')

id_list = rec_list['IdList']
handle = Entrez.efetch(db='nucleotide', id=id_list, rettype='gb')
recs = list(SeqIO.parse(handle, 'gb'))
handle.close()

L = []

for record in recs:
        L.append(record)

SeqIO.write(L,"%s_%s.fasta" % (species,gene),"fasta")
