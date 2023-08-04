import os
import pickle

# Replace "input_directory" with the path to the directory containing your input FASTQ files
input_directory = "input"

# List all files in the input directory
input_files = os.listdir(input_directory)
print('check1')
# Extract sample names from the filenames and create the SAMPLES list
SAMPLES = []
for filename in input_files:
    if filename.endswith("_1.fastq"):
        sample_name = filename.replace("_1.fastq", "")
        SAMPLES.append(sample_name)

# Print the SAMPLES list so that we can pass it to the Snakemake workflow as a command-line argument
#print("SAMPLES:", SAMPLES)

with open("sample_list.pkl", "wb") as f:
    pickle.dump(SAMPLES, f)