1.Input folder contians the paired end metagenomic sequencing reads for each group (weigh-loss, adult and cancer/IBD)

2.Output directories are named according the the database, k size (used during gather step) and input group.
- Naming scheme : {group-name}.{ksize}.{database_shorthand}. For eg, weight_loss.51.genome


| Database                       | databases_shorthand   | file_name                          |
|--------------------------------|-------------|------------------------------------|
| Crop's chloroplast genome      | crop_genome | db.crop-plant-entrez-ref.fasta.bz2 |
| All plant's chloroplast genome | genome      | db.plant-entrez-ref.fasta.bz2      |
| Crop's trnL gene               | crop_trnl   |                                    |
| All plants trnL gene           | trnl        | db.trnL-entrez-ref.fasta.bz2       |

- Each output folder has 3 sub-folders: Sketches,gather, and cmon_name_annot. 

3.join_common_name_dbs.py is the python script which annontates the gather matches with common names from different sources (FooDB, USDA etc)
