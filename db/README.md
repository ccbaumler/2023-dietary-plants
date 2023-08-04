The directory contains compressed databases.

- Common-name-cleaned is a directory with cleaned csv(FoodB,USDA,trnL.names) files to use for common name annotation
- Common-name-cleaned is a directory with the raw files from different sources (FoodB,USDA,trnL.names).

- db.trnL-entrez-ref.fasta.bz2 is a database containing all available trnL genes on NCBI.
- [db.plant-entrez-ref.fasta.bz2](https://farm.cse.ucdavis.edu/~baumlerc/raw-db/db.plant-entrez-ref.fasta.bz2) is a database containing all available trnL-containing plant genomes on NCBI.
- trnLGH.fasta.gz is a dietary trnL database for PCR results curated by Petrone et al (2023) https://doi.org/10.1073/pnas.2304441120

These are also available for direct download at https://farm.cse.ucdavis.edu/~baumlerc/raw-db/

To create a sourmash database from the fasta databases, use:

`sourmash sketch dna -p scaled=1,k=11 --singleton <fasta.db> -o <fasta.db.k11.zip>`

### Sources for databases
- db.trnL.names.csv.gz is the taxonomic metadata database for all the trnL genes (and their plant genomes) on the NCBI.
- FooDB_data.zip source: https://foodb.ca/downloads
- USDA_data.csv source: https://plants.usda.gov/home/downloads
