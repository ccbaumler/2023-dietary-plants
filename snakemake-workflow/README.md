- Input folder contians the paired end metagenomic sequencing reads for each group (weigh-loss, adult and cancer/IBD)
- Output directories are named according the the database, k size (used during gather step) and input group. Each output folder has 3 sub-folders: Sketches,gather, and cmon_name_annot. 

- join_common_name_dbs.py is the python script which annontates the gather matches with common names from different sources (FooDB, USDA etc)
