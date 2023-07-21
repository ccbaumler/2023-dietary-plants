The directory contains compressed databases.

- db.trnL-entrez-reps.fasta.gz is a database containing all available trnL genes on NCBI.
- trnLGH.fasta.gz is a dietary trnL database for PCR results curated by Petrone et al (2023) https://doi.org/10.1073/pnas.2304441120

To create a sourmash database from the fasta databases, use:
`sourmash sketch dna -p scaled=1,k=11 --name-from-first --singleton <fasta.db> -o <fasta.db.k11.zip>
