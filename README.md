# NCBI-request-scripts
This repesotiry contains homemade scripts to facilitate accession of sequences from the ncbi nucleotide database. All script rely on the biopython and entrez packages, and require Biopython to be installed.

# species_request.py: 

This script takes genus, species and gene as an entry and download matched sequences from the NCBI nucleotide database.

Note that the default maximum of downloaded sequences is set to 20, this can be modified.

Usage: $ species_request.py email Genus species gene


# genus_request.py: 

This script takes genus and gene as an entry and download matched sequences from the NCBI nucleotide database.

Note that the default maximum of downloaded sequences is set to 20, this can be modified.

Usage: $ genus_request.py email Genus gene 
