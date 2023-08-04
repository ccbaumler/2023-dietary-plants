This directory contains scirpts used for analysis

- join_common_name.py is a python script to annotate scientific names in prefetch/gather results with the common name.
- generate_samples.py is a python script which uses the input directory to find all sample names to parse into the snakefile. It saves a list all samples in a pkl (pickle) file
- Common-name-clean-nbs is a folder housing python notebooks (.ipynb) used for extracting relevant features from the FooDB/USDA/trnl common name sources databases. The output file summarizing relevant FooDB data is under db/common_name.csv
