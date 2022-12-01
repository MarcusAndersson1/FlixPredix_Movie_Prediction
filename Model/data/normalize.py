import numpy as np
import pandas as pd
import json
import os

# Print current directory (for debugging)
    # print(os.getcwd()) 


# Create dataframe from CSV file
df = pd.read_csv('Model/data/tmdb_5000_movies.csv', sep=',')
# Remove unwanted features from Dataframe
df = df.drop('homepage', axis=1).drop('id', axis=1).drop('keywords', axis=1).drop('overview', axis=1).drop('release_date', axis=1).drop('status', axis=1).drop('tagline', axis=1).drop('title', axis=1).drop('original_title', axis=1)

# Split genres into separate columns (e.g. 'genres'-> 'genre_western' and 'genre_comedy')
genres = df.loc[:, 'genres']
genres_normalized = []

for genre in genres:
    data = json.loads(genre)
    names = list(map(lambda x: x['name'].replace(" ", "_").lower(), data))
    genres_normalized.append(names)


df['genres_normalized'] = genres_normalized

df1 = (
    df['genres_normalized'].explode()
    .str.get_dummies().groupby(level=0).sum().add_prefix('genres_')
)


df = df.drop('genres', axis=1).drop('genres_normalized', axis=1).join(df1)

# Split production countries into separate columns

production_countries = df.loc[:, 'production_countries']
production_countries_normalized = []

for production_country in production_countries:
    data = json.loads(production_country)
    names = list(map(lambda x: x['name'].replace(" ", "_").lower(), data))
    production_countries_normalized.append(names)


df['production_countries_normalized'] = production_countries_normalized

df2 = (
    df['production_countries_normalized'].explode()
    .str.get_dummies().groupby(level=0).sum().add_prefix('country_') # shortened it from production_country to just country
)


df = df.drop('production_countries', axis=1).drop('production_countries_normalized', axis=1).join(df2)

# Split spoken languages into separate columns (MIGHT NOT BE USED)

# spoken_languages = df.loc[:, 'spoken_languages']
# spoken_languages_normalized = []

# for spoken_language in spoken_languages:
#     data = json.loads(spoken_language)
#     names = list(map(lambda x: x['iso_639_1'].replace(" ", "_").lower(), data))
#     spoken_languages_normalized.append(names)


# df['spoken_languages_normalized'] = spoken_languages_normalized

# df2 = (
#     df['spoken_languages_normalized'].explode()
#     .str.get_dummies().groupby(level=0).sum().add_prefix('spoken_language_')
# )


# df = df.drop('spoken_languages', axis=1).drop('spoken_languages_normalized', axis=1).join(df2)


# Remove movies with 0 or null runtime
df = df.loc[(df[['runtime', 'budget']] != 0).all(axis=1)]
df = df[df['runtime'].notna()]


# Create new modified CSV file for training usage
df.to_csv('normalized.csv')
