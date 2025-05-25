# src/scraping.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_imdb_top_250():
    url = "https://www.imdb.com/chart/top"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = soup.select('td.titleColumn')
    ratings = soup.select('td.imdbRating strong')

    movie_data = []
    for movie, rating in zip(movies, ratings):
        name = movie.a.text
        year = movie.span.text.strip("()")
        rank = movie.get_text(strip=True).split('.')[0]
        rating = rating.text

        movie_data.append({
            'rank': int(rank),
            'name': name,
            'year': int(year),
            'rating': float(rating)
        })

    df = pd.DataFrame(movie_data)
    df.to_csv('data/imdb_top_250_movies.csv', index=False)
    print("✅ Data scraped and saved to 'data/imdb_top_250_movies.csv'")

if __name__ == "__main__":
    scrape_imdb_top_250()
