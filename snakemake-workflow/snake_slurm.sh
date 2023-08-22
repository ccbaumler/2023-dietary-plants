#! /bin/bash -login
#SBATCH -p bmh
#SBATCH -J plant_dna
#SBATCH -t 5-10:00:00
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 8
#SBATCH --mem=60gb
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sjnair@ucdavis.edu
#SBATCH -o /home/sjnair/2022-benchmark/sourmash-gather/output/reports/slurm-%j.out
#SBATCH -e /home/sjnair/2022-benchmark/sourmash-gather/output/reports/slurm-%j.err

# activate conda
. "/home/sjnair/miniconda3/etc/profile.d/conda.sh"

# activate sourmash env
conda activate snakemake

# run snakefile 
snakemake -s Snakefile -c 8 --rerun-incomplete -k