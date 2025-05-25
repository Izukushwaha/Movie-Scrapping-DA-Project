
# src/analysis.py

import pandas as pd
from preprocessing import load_and_clean_data

def summary_statistics(df):
    stats = df.describe()
    print("Summary Statistics:\n", stats)

def decade_analysis(df):
    return df.groupby('decade')['rating'].agg(['mean', 'count'])

def find_outliers(df):
    q1 = df['rating'].quantile(0.25)
    q3 = df['rating'].quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df['rating'] < q1 - 1.5 * iqr) | (df['rating'] > q3 + 1.5 * iqr)]
    return outliers

if __name__ == "__main__":
    df = load_and_clean_data()
    summary_statistics(df)
    print("\nDecade-wise Analysis:\n", decade_analysis(df))
    print("\nOutliers:\n", find_outliers(df))
