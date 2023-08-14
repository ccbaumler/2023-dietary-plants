import os
import pandas as pd

def main():
    input_directory = "../snakemake-workflow/benchmarks"
    output_file = "benchmark.report.tsv"

    combo = "all.benchmarks.tsv"

    combine_tsvs(input_directory, combo) 

    grouped_data = calculate_values(combo)
    grouped_data.to_csv(output_file, sep='\t')

def calculate_values(fp):
    df = pd.read_csv(fp, sep="\t")
    df = df.drop(columns=["h:m:s"])
    
    agg_columns = ["s", "max_rss"]#, "max_vms", "max_uss", "max_pss", "mean_load", "cpu_time"]
    agg_functions = ["mean", "max", "min"]
    grouped = df.groupby("filename")[agg_columns].agg(agg_functions)
    grouped.columns = [f"{col}_{agg}" for col in grouped.columns.levels[0] for agg in grouped.columns.levels[1]]
    
    return grouped

    group = df.groupby("filename").agg(
            s_mean=pd.NamedAgg(column="s", aggfunc='mean'),
            s_min=pd.NamedAgg(column="s", aggfunc='min'),
            s_max=pd.NamedAgg(column="s", aggfunc='max'),
            max_rss_mean=pd.NamedAgg(column="max_rss", aggfunc='mean'),
            max_rss_min=pd.NamedAgg(column="max_rss", aggfunc='min'),
            max_rss_max=pd.NamedAgg(column="max_rss", aggfunc='max'),
            )          
    return group    

def combine_tsvs(input_dir, output):
    #try os.walk and fn
    #ls_filenames = [ x for x in glob('*.{}'.format('tsv')) ] #This gives a list of all files in working dir
    for root, dirs, files in os.walk(f'{input_dir}'):
        ls_filenames= [ str.rsplit(file, sep='.', maxsplit=1)[0] for file in files]
    
    dataframes = []

    for fp in sorted(ls_filenames):
        df = pd.read_csv(input_dir + "/" + fp + ".tsv", sep='\t')
        df['filename'] = fp
        dataframes.append(df)

    combined_tsv = pd.concat(dataframes)
    combined_tsv.to_csv(output, sep='\t', index=False)

if __name__ == "__main__":
    main()
