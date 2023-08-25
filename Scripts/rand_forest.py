import pandas as pd
import sys
import os
import zipfile
import json
import glob
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import warnings


def fetch_files(group,db,scale,k):
    hash_matches_path = f"..\\snakemake-workflow\\output\\{group}\\{db}.{scale}\\hash_matches\\"
    ext = f"*{k}.query-matches.sig"

    target_files = glob.glob(os.path.join(hash_matches_path,ext))
    return target_files



def sig2dict(target_files):    
    data_dict ={}
    for i in range(len(target_files)):
        sample = target_files[i].split('\\')[-1].split('.')[0]
        with open(target_files[i]) as f:
            js = json.loads(f.read())
        data_dict[sample] = [js[0]['signatures'][0]['mins'],js[0]['signatures'][0]['abundances']]
    return data_dict


def dict2df(data_dict):
    df = pd.DataFrame(index=data_dict.keys())
    for sample, (hashes, values) in data_dict.items():
        for hash_val, value in zip(hashes, values):
            df.loc[sample, hash_val] = value #slow and defragmented? apparently

    # Fill NaN values with 0
    return df.fillna(0)

def group_df(group,db,scale,k):
    group_files = fetch_files(group,db,scale,k)
    group_dict = sig2dict(group_files)
    group_df = dict2df(group_dict)
    group_df['group'] = group
    return group_df

def combine_groups(group1_df, group2_df):   
    combined_df = pd.concat([group1_df,group2_df], axis=0)
    combined_df = combined_df.fillna(0)
    return combined_df
    
def fit_rf(combined_df,output_dir):    
    y = combined_df['group']
    X = combined_df.drop('group',axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

    # Build the confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    # Display the confusion matrix using a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.title("Confusion Matrix")
    plt.savefig(os.path.join(output_dir, "confusion_matrix.png"))

    # feature importance
    feature_importances = model.feature_importances_
    importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances})
    importance_df = importance_df.sort_values(by='Importance', ascending=False)
    importance_df.to_csv(os.path.join(output_dir, "feature_imp.csv"), index=False)

if __name__ == "__main__":
    group1 = str(sys.argv[1])
    group2= str(sys.argv[2])
    db = str(sys.argv[3])
    scale = str(sys.argv[4])
    k =str(sys.argv[5])
    output_dir = str(sys.argv[6])

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    warnings.filterwarnings('ignore')
    group1_df = group_df(group1,db,scale,k)
    group2_df = group_df(group2,db,scale,k)

    combined_df = combine_groups(group1_df,group2_df)
    fit_rf(combined_df, output_dir)
    print("woop woop")