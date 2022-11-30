import numpy as np
import pandas as pd
import json


df = pd.read_csv('tmdb_5000_movies.csv', sep=',')

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

