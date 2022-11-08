import sys
from Bio import Entrez, SeqIO

usage = 'Usage: ' + sys.argv[0] + ' email Genus gene '

if len(sys.argv) != 4:
    print(usage)
    exit()

email = sys.argv[1]
genus = sys.argv[2]
gene = sys.argv[3]

Nbsequences = input('How many sequences do you want to download (max) ?')

Entrez.email = "%s" % (email)

handle = Entrez.esearch(db="nucleotide", term='%s AND "%s"[Organism]' % (gene, genus), retmax = Nbsequences)
rec_list = Entrez.read(handle)
handle.close()

nbrecords = len(rec_list['IdList'])
print('the ncbi nucleotide database had', nbrecords, 'sequences corresponding to your request')

if nbrecords == 0:
    exit()

id_list = rec_list['IdList']
handle = Entrez.efetch(db='nucleotide', id=id_list, rettype='gb')
recs = list(SeqIO.parse(handle, 'gb'))
handle.close()

L = []

for record in recs:
        L.append(record)

SeqIO.write(L,"%s_%s.fasta" % (genus,gene),"fasta")
