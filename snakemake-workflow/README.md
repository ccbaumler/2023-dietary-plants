1. Input folder contians the paired end metagenomic sequencing reads for each group (weigh-loss, adult and cancer/IBD)
- Use this workflow with the `snakemake -s Snakefile -j 32 --use-conda --latency-wait 30 --rerun-incomplete` command!


2. The output directory contains a sequence group directory which contains database-specific directories. The final files per database per group are stored in the directories, gather and cmon_name_annot.
```
~/2023-dietary-plants/snakemake-workflow
   |--input
   |----weight_loss
   |--output
   |----weight_loss
   |------all_chloroplast
   |--------cmon_name_annot
   |--------gather
   |------crop_chloroplast
   |--------cmon_name_annot
   |--------gather
   |------sketches
```

- File naming scheme : {database_shorthand}.{sample}.{k-size}.{output_type}. 
    - `sourmash gather` output = output/weight_loss/crop_chloroplast/gather/crop_chloroplast.ERR11520726.51.gather.csv
    - `join_common_name_dbs.py` output = output/weight_loss/crop_chloroplast/cmon_name_annot/crop_chloroplast.ERR11520726.51.annot.gather.csv

| Database                       | databases_shorthand   | file_name                          |
|--------------------------------|-------------|------------------------------------|
| Crop's chloroplast genome      | crop_chloroplast | db.crop-plant-entrez-ref.fasta.bz2 |
| All plant's chloroplast genome | all_chloroplast  | db.plant-entrez-ref.fasta.bz2      |
| Crop's trnL gene               | crop_trnl   |                                    |
| All plants trnL gene           | all_trnl    | db.trnL-entrez-ref.fasta.bz2       |


3. `join_common_name_dbs.py` is the python script which annontates the gather matches with common names from different sources (FooDB, USDA etc)
