This directory houses all contents for a preliminary attempt to annotate prefetch results with common names of dietary plants.

Contents:
1. test_data/prefetch_data.csv: This was the results from running prefetch from a weight loss sample from the stool plant dna against the trnL database
2. prefetch_annontate_trial.ipynb: Python notebook which was used to filter prefetch results which were also present in the FooDB db, and annotate prefetch results with the common name of dietary plants
3. Prefetch_annotate.csv: The final file which contains prefetch results annotated with dietary plant's common name

Conclusions:
The prefetch results had 5015 matches; FoodBD has 240 unique common names entries. The intersection between these files is around 101. Ie 101 out of 5015 prefetch matches can be annotated by FooDB data. Might have to look into a better database for more coverage.
