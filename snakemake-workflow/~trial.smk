import os
#import pickle

configfile: "config.yaml"

group = config.get("group")
indir = [os.path.join("input", dir_name) for dir_name in group]

#print(indir)

SAMPLES_DICT = {}
for path in indir:
    for (dirpath, dirnames, filenames) in os.walk(path):
        dir_name = os.path.basename(dirpath)
        SAMPLES_DICT[dir_name] = [filename.split('_')[0] for filename in filenames][:2]
        break
#print(config["dbs"])

#list_all_inputs = [ 
#    expand(
#        f"output/{group_id}/{{db}}/cmon_name_annot/{{db}}.{sample_id}.{{k}}.annot.gather.csv",  db=config["dbs"], k=config["k_size"]
#        ) 
#    for group_id, sample_list in SAMPLES_DICT.items() for sample_id in sample_list ]

all_inputs=[]
for db,filepath in config["dbs"].items():
    if db == 'trnl':
        list_trnl = [expand(f"output/{group_id}/{{db}}/cmon_name_annot/{{scale}}.{sample_id}.{{k}}.annot.gather.csv", scale=100, db=db, k =config["k_size"]) for group_id, sample_list in SAMPLES_DICT.items() for sample_id in sample_list]
        all_inputs.append(list_trnl)
    else:
        list_entrez = [expand(f"output/{group_id}/{{db}}/cmon_name_annot/{{scale}}.{sample_id}.{{k}}.annot.gather.csv",scale=config["scale"], db=db, k =config["k_size"]) for group_id, sample_list in SAMPLES_DICT.items() for sample_id in sample_list]
        all_inputs.append(list_entrez)

print(f"{SAMPLES_DICT}")
print("----------------------------------------")
print(f"TRNL {len(list_trnl)} , {len(list_trnl[0])})")
print("-----------------------")
print(f"all inputs {len(all_inputs), len(all_inputs[0]), len(all_inputs[0][0])} )")

print("----------------------------------------")
print(f"ENTEREZ {list_entrez}")


#def extract_samples():
#    input_directory = "input/"+config["group"]
#    input_files = os.listdir(input_directory)
#    # Extract sample names from the filenames and create the SAMPLES list
#    SAMPLES = []
#    for filename in input_files:
#        if filename.endswith("_1.fastq.gz"):
#            sample_name = filename.replace("_1.fastq.gz", "")
#            SAMPLES.append(sample_name)
#    return SAMPLES

# Function to load SAMPLES list from pickle file
#def load_samples():
#    with open("sample_list.pkl", "rb") as f:
#        return pickle.load(f)

#SAMPLES = extract_samples()

# Another method for ustilizing a config file in snakemake to the fullest
#def get_wildcards(wildcards):
#    return config["dbs"][wildcards.db]
#    return config["k_size"][wildcards.k]

#def name_scheme():
#    if config["db"] == './../Sketched-db/db.crop-plant-entrez.ref.sig.zip':
#        return config["group"]+"."+config["k"]+"."+"crop_genome"
#    else:
#        return config["group"]+"."+config["k"]+"."+"genome"


#dir_name = name_scheme()
#SAMPLES = extract_samples()
# test rule
#rule test:
#   shell:
#        """
#        echo "hello"
#        """


# SNAKEMAKE RULES
rule all:
   input:
        #expand("output/{group}/{db}/cmon_name_annot/{scale}.{sample}.{k}.annot.gather.csv",  db=config["dbs"] ,sample=SAMPLES, k=config["k_size"])
        list_entrez,
        list_trnl

# Rule for running Sourmash sketch
rule run_sourmash_sketch:
    input:
        r1="input/{group}/{sample}_1.fastq.gz",
        r2="input/{group}/{sample}_2.fastq.gz"
    output:
        "output/{group}/sketches/{sample}.sig.zip"
    #conda:
    #   "sourmash.yml"
    shell:
        "sourmash sketch dna -p scaled=100,k=21,k=31,k=51,abund {input.r1} {input.r2} --name '{wildcards.sample}' -o {output}"

# Rule for running Sourmash gather
rule run_sourmash_gather:
    input:
        "output/{group}/sketches/{sample}.sig.zip"
    output:
        gather_csv ="output/{group}/{db}/gather/{scale}.{sample}.{k}.gather.csv",
        prefetch_sigs= "output/{group}/{db}/gather_ext/{scale}.{sample}.{k}.prefetch.sig",
        gather_matches = "output/{group}/{db}/gather_ext/{scale}.{sample}.{k}.gather.csv",
        prefetch_csv = "output/{group}/{db}/gather_ext/{scale}.{sample}.{k}.prefetch.csv",
    #conda:
    #   "sourmash.yml"
    params:
        # Access the file name instead of the assigned name
        db_file = lambda wildcards:config["dbs"][wildcards.db],
        #k = config["k"]
    shell:
        #"sourmash prefetch {input} db.trnL-entrez-ref.fasta.sig --dna --ksize 51 --threshold-bp 0 -o {output}" #save prefetch results
        "sourmash gather {input} {params.db_file} --threshold-bp 0 -k87 {wildcards.k} --save-matches {output.gather_matches} --save-prefetch {output.prefetch_sigs} --save-pretech-csv {output.prefetch_csv} -o {output.gather_csv}" 

# Rule for performing inner join with common_names.csv
rule perform_inner_join:
    input:
       "output/{group}/{db}/gather/{scale}.{sample}.{k}.gather.csv" ,
    output:
       "output/{group}/{db}/cmon_name_annot/{scale}.{sample}.{k}.annot.gather.csv" #{db.{ksize}.{sample}.common.csv
    shell:
       "python join_common_name_dbs.py {input} {output}"

