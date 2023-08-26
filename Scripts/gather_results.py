import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def agg_df(group):
    folder_paths =[f"../snakemake-workflow/output/{group}/all_chloroplast.100/cmon_name_annot/",
              f"../snakemake-workflow/output/{group}/all_chloroplast.1000/cmon_name_annot",
              f"../snakemake-workflow/output/{group}/crop_chloroplast.100/cmon_name_annot/",
              f"../snakemake-workflow/output/{group}/crop_chloroplast.1000/cmon_name_annot/",
              f"../snakemake-workflow/output/{group}/trnl.100/cmon_name_annot/"
              ]
    dataframes=[]
    for folder_path in folder_paths:
        files = os.listdir(folder_path)
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(folder_path, file)
                df = pd.read_csv(file_path)
                dataframes.append(df)
    final_df = pd.concat(dataframes, ignore_index=True)
    return(final_df)

def db_shorthand(filename):
    return filename.split('/')[2].split('.')[0]

def cmon_name_col(df): # combines the 3 sources into one column. Priority given to USDA first.
    priority_order =['usda_common_name','trnl_common_name','foodb_common_name']
    df['common_name'] = df['usda_common_name']
    for column in priority_order[1:]:
        df['common_name'] = df['common_name'].combine_first(df[column])
    return df

def make_charts(final_df):
    grouped = final_df.groupby(['query_name', 'ksize', 'scaled','db']).size().reset_index(name='match_count')
    grouped_2 = final_df.dropna(subset=['common_name'], inplace=False).groupby(['query_name', 'ksize', 'scaled','db']).size().reset_index(name='common_name_match_count')
    # Set up the subplots
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

    # Plot the first box plot
    sns.boxplot(x='scaled', y='match_count', hue='ksize', data=grouped[grouped['db'] == 'all_chloroplast'], ax=axes[0,0])
    axes[0,0].set_title('all_chloroplast')

    # Plot the second box plot
    sns.boxplot(x='scaled', y='match_count', hue='ksize', data=grouped[grouped['db'] == 'crop_chloroplast'], ax=axes[0,1])
    axes[0,1].set_title('crop_chloroplast')

    # Plot the third box plot
    sns.boxplot(x='scaled', y='match_count', hue='ksize', data=grouped[grouped['db'] == 'trnl'], ax=axes[0,2])
    axes[0,2].set_title('trnl')


    # Plot the first box plot
    sns.boxplot(x='scaled', y='common_name_match_count', hue='ksize', data=grouped_2[grouped_2['db'] == 'all_chloroplast'], ax=axes[1,0])
    axes[1,0].set_title('all_chloroplast')

    # Plot the second box plot
    sns.boxplot(x='scaled', y='common_name_match_count', hue='ksize', data=grouped_2[grouped_2['db'] == 'crop_chloroplast'], ax=axes[1,1])
    axes[1,1].set_title('crop_chloroplast')

    # Plot the third box plot
    sns.boxplot(x='scaled', y='common_name_match_count', hue='ksize', data=grouped_2[grouped_2['db'] == 'trnl'], ax=axes[1,2])
    axes[1,2].set_title('trnl')

    # Adjust layout and show the plots
    plt.suptitle("Box plot of number of gather matches for different databases")
    plt.tight_layout()
    plt.savefig("boxplots.png")



if __name__ == "__main__":
    final_df = agg_df(sys.argv[1])

    final_df['db'] = final_df['filename'].apply(db_shorthand)

    final_df= cmon_name_col(final_df)
   


    make_charts(final_df)