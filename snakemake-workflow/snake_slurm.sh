#! /bin/bash -login
#SBATCH -p bmh
#SBATCH -J chr_weightlos
#SBATCH -t 20:00:00
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 10
#SBATCH --mem=50gb
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sjnair@ucdavis.edu
#SBATCH -o /home/sjnair/reports/slurm-%j.out
#SBATCH -e /home/sjnair/reports/slurm-%j.err

# activate conda
. "/home/sjnair/miniconda3/etc/profile.d/conda.sh"

# activate sourmash env
conda activate snakemake

# run snakefile 
snakemake -s Snakefile -c 10 -k