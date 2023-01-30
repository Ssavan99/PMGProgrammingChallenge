#!/usr/bin/env python3

import sys
import pandas as pd
import os

def addColumn(df, file):
    df['filename'] = [file for item in range(len(df))]
    return df

def csv_combiner(combine_csv, new_df):
    combine_csv = pd.concat([combine_csv, new_df])
    return combine_csv
    
def main():
    if len(sys.argv) <= 1:
        print("No input files")
        
    files = sys.argv[1:]
    fileName = [os.path.basename(file) for file in files]
    print(files)
    combine_csv = pd.DataFrame()
    
    for i in range(len(files)):
        df = pd.read_csv(files[i])
        new_df = addColumn(df, fileName[i])
        combine_csv = csv_combiner(combine_csv, new_df)
    
    final_csv = combine_csv.to_csv('combine_csv')
    

if __name__ == "__main__":
    main()