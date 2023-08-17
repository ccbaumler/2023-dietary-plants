The directory contains compressed databases.

- Common-name-cleaned is a directory with cleaned csv(FoodB,USDA,trnL.names) files to use for common name annotation
  
- Common-name-cleaned is a directory with the raw files from different sources (FoodB,USDA,trnL.names).

- db.trnL-entrez-ref.fasta.bz2 is a database containing all available trnL genes on NCBI.
  
- [db.plant-entrez-ref.fasta.bz2](https://farm.cse.ucdavis.edu/~baumlerc/raw-db/db.plant-entrez-ref.fasta.bz2) is a database containing all available trnL-containing plant chloroplast genomes on NCBI.

- [GRCh38.p14.100.zip](https://farm.cse.ucdavis.edu/~baumlerc/raw-db/GRCh38.p14.100.zip) and [GRCh38.p14.1000.zip](https://farm.cse.ucdavis.edu/~baumlerc/raw-db/GRCh38.p14.1000.zip) are sourmash signatures (scaled=100 and 1000, respectively) of the most recent (as of 08/16/2023) human reference genome at:
  - https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001405.40/
  - https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.40_GRCh38.p14/

- [db.plastid.100.zip](https://farm.cse.ucdavis.edu/~baumlerc/raw-db/db.plastid.100.zip) and [db.plastid.1000.zip](https://farm.cse.ucdavis.edu/~baumlerc/raw-db/db.plastid.1000.zip) are sourmash sketched (scaled=100 and 1000, respectively) of the most recent (as of 08/16/2023) NCBI plastid genome database
  - https://ftp.ncbi.nlm.nih.gov/refseq/release/plastid/
  - https://www.ncbi.nlm.nih.gov/genome/organelle/ 

- trnLGH.fasta.gz is a dietary trnL database for PCR results curated by Petrone et al (2023) https://doi.org/10.1073/pnas.2304441120

These are also available for direct download at https://farm.cse.ucdavis.edu/~baumlerc/raw-db/

To create a sourmash database from the fasta databases, use:

`sourmash sketch dna -p scaled=1,k=11 --singleton <fasta.db> -o <fasta.db.k11.zip>`

### Sources for databases
- db.trnL.names.csv.gz is the taxonomic metadata database for all the trnL genes (and their chloroplast genomes) on the NCBI.
- FooDB_data.zip source: https://foodb.ca/downloads
- USDA_data.csv source: https://plants.usda.gov/home/downloads
