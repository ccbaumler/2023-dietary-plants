import sys
import pandas as pd

def match_strings(csv_file1, csv_file2, column_name1, column_name2):
    # Read the CSV files into pandas DataFrames
    df1 = pd.read_csv(csv_file1)
    df2 = pd.read_csv(csv_file2)
    #check if everything is in order
    if column_name1 not in df1.columns:
        raise ValueError(f"Column '{column_name1}' not found in {csv_file1}")
    if column_name2 not in df2.columns:
        raise ValueError(f"Column '{column_name2}' not found in {csv_file2}")

    matched_data = pd.DataFrame(columns=[column_name1, column_name2])

    # Iterate through each row of df1 and find matches in df2
    for index, row in df1.iterrows():
        value_to_match = row[column_name1]
        matches = df2[df2[column_name2].str.contains(value_to_match, case=False)]
        if not matches.empty:
            matched_data = pd.concat([matched_data, pd.DataFrame({column_name1: [value_to_match],
                                                                  column_name2: [", ".join(matches[column_name2])]},
                                                                 index=[len(matched_data)])],
                                     ignore_index=True)

    return matched_data

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py csv_file1 csv_file2 column_name1 column_name2")
        sys.exit(1)

    csv_file1 = sys.argv[1]
    csv_file2 = sys.argv[2]
    column_name1 = sys.argv[3]
    column_name2 = sys.argv[4]

    try:
        result = match_strings(csv_file1, csv_file2, column_name1, column_name2)
        print("Matching Results:")
        print(result)
    except Exception as e:
        print("Error:", e)
