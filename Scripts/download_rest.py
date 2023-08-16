import subprocess
import os

with open("acc_list.txt") as f:
        samples = [line.strip() for line in f]

list_dr = os.listdir("../snakemake-workflow/input/adult-1/")

for i in samples:
    if samples[i]+"_1"+".fastq.gz" is in list_dr and sample

