# NCBI-request-scripts
This repesotiry contains homemade scripts to facilitate accession of sequences from the ncbi nucleotide database. All script rely on the biopython and entrez packages, and require Biopython to be installed.

For all scripts an email adress has to be submitted

# species_request.py: 

This script takes genus, species and gene as an entry and download matched sequences from the NCBI nucleotide database.

Usage: $ species_request.py email Genus species gene


# genus_request.py: 

This script takes genus and gene as an entry and download matched sequences from the NCBI nucleotide database.

Usage: $ genus_request.py email Genus gene 
