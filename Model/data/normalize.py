import numpy as np
import pandas as pd
import json


df = pd.read_csv('tmdb_5000_movies.csv', sep=',')

df = df.drop('homepage', 1).drop('id', 1).drop('keywords', 1).drop('overview', 1).drop('release_date', 1).drop('status', 1).drop('tagline', 1).drop('title', 1).drop('original_title', 1)

genres = df.loc[:, 'genres']
genres_normalized = []

for genre in genres:
    data = json.loads(genre)
    names = list(map(lambda x: x['name'].replace(" ", "_").lower(), data))
    genres_normalized.append(names)


df['genres_normalized'] = genres_normalized

df1 = (
    df['genres_normalized'].explode()
    .str.get_dummies().sum(level=0).add_prefix('genres_')
)

df = df.drop('genres', 1).drop('genres_normalized', 1).join(df1)

df.to_csv('normalized.csv')

