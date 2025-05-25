# src/visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from preprocessing import load_and_clean_data

def plot_rating_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['rating'], bins=10, kde=True)
    plt.title('IMDb Rating Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.savefig('output/charts/rating_distribution.png')
    plt.close()

def plot_movies_by_decade(df):
    decade_counts = df['decade'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=decade_counts.index, y=decade_counts.values)
    plt.title('Number of Top Movies by Decade')
    plt.xlabel('Decade')
    plt.ylabel('Number of Movies')
    plt.savefig('output/charts/movies_by_decade.png')
    plt.close()

if __name__ == "__main__":
    df = load_and_clean_data()
    plot_rating_distribution(df)
    plot_movies_by_decade(df)
