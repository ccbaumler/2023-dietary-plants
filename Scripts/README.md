This directory contains scirpts used for analysis

- Common-name-clean-nbs is a folder housing python notebooks (.ipynb) used for extracting relevant features from the FooDB/USDA/trnl common name sources databases. The output file summarizing relevant FooDB data is under db/common_name.csv
- download_ENA.sh downloads projects fromm the ENA site.
- gather_results.py provides an overview of all parameter combinations for a group of samples. It outputs a box-plot comparing the number of matches and a html file which lists the most abundant sample.
- rand_forest.py converts matching sigs from prefetch output to a abundance weighted matrix with rows representing samples and columns representing hashes. It then fits a Random Forest model to classify samples into two groups. Finally it outputs a confusion matrix and csv of feature importance
