import sys
import pandas as pd

#results = pd.read_csv('../test/test_data/prefetch_trial.csv')
input_path = sys.argv[1]
results = pd.read_csv(input_path)
final_FooDB = pd.read_csv('../db/Common-name-cleaned/final_FooDB.csv')
final_trnl =pd.read_csv('../db/Common-name-cleaned/final_trnl.csv')
final_USDA = pd.read_csv('../db/Common-name-cleaned/final_USDA.csv')

def std_name(name):
    word_list = name.split()
    #accession,region = word_list[0].split(':')

    sci_name = word_list[1]+' '+word_list[2]
    other = ' '.join(word_list[2:])
    #return accession,region,sci_name,other
    return sci_name

#split match_name
#results['scientific_name'] = results['match_name'].apply(lambda x: pd.Series(std_name(x))) #For prefetch
results['scientific_name'] = results['name'].apply(lambda x: pd.Series(std_name(x)))

#joins
results = results.merge(final_USDA, on='scientific_name',how='left')
results = results.merge(final_trnl, on='scientific_name',how='left')
results = results.merge(final_FooDB, on='scientific_name',how='left')

#print summary

num_rows_with_na_all_cols = results[['usda_common_name', 'foodb_common_name', 'trnl_common_name']].isna().all(axis=1).sum()
print(f'Out of {results.shape[0]} matches,{results.shape[0] - num_rows_with_na_all_cols} were annotated with common names')
print(sys.argv[1])