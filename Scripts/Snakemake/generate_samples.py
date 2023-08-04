import os

# Replace "input_directory" with the path to the directory containing your input FASTQ files
input_directory = "path/to/your/input_directory"

# List all files in the input directory
input_files = os.listdir(input_directory)

# Extract sample names from the filenames and create the SAMPLES list
SAMPLES = []
for filename in input_files:
    if filename.endswith("_1.fastq"):
        sample_name = filename.replace("_1.fastq", "")
        SAMPLES.append(sample_name)

# Print the SAMPLES list so that we can pass it to the Snakemake workflow as a command-line argument
print("SAMPLES:", SAMPLES)
