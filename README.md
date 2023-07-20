# 2023-dietary-plants
Bioinformatically barcode the diet from stool metagenome samples

The overarching hypothesis is that sourmash and the software tools in the lab have created a wonderful system to computationally perform DNA metabarcoding.

The main hypothesis is that the trnL chloroplast gene barcode reflects the dietary quality of an individual and DNA barcodes are able to be bioinfomatically identified in metagenome with the lab software.

Ideas to investigate:
- Think about requesting the author’s menu and daily diet log data from https://www.pnas.org/doi/abs/10.1073/pnas.2304441120
  - Requesting the author’s data could be a robust experimental set to add to the computational data we gather for ML
- Rule out background by randomly searching metagenomes? Do we see much dietary taxonomies or are their non-dietary plants included from the search?
- Are results better with full plant genomes of known dietary plants?
- Are results better with only dietary plant trnL genes or a full database of plant trnL genes?
- How do results change with different parameters?
- Do the genes correlate to a particular metagenome (mastiff/branchwater) do the metagenomes correlate with a particular taxonomic unit (prefetch/gather)?
- If these correlations/results are quatifiably good can we use a classifier for further examine the corollary information?


Questions to answer:
- Why this cholorplast gene marker (greater survival or abundance)?
- Is there a dietary plant taxonomy database?
- How does animal taxa correlated with a specific gene (trnL, rbcL, ITS, CO1, 12s, 16s, 18s, SSU)?
