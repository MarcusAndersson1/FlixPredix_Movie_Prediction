import numpy as np
import pandas as pd
import json
import logging

logging.basicConfig(level=logging.INFO) # switch to logging.DEBUG for more info

logger = logging.getLogger('normalize')


REGIONS = {
    'NA': ['US', 'CA', 'BS', 'MX', 'DM', 'GP'],
    'SA': ['AR', 'AW', 'BR', 'BO', 'CL', 'CO', 'DO', 'EC', 'PA', 'PE'],
    'UK': ['GB', 'IE'],
    'EU': ['AF', 'AT', 'BA', 'BE', 'BG', 'CH', 'CS', 'CZ', 'DE', 'DK', 'ES', 'FI', 'FR', 'GR', 'HU', 'IS', 'IT', 'LT', 'LU', 'MA', 'MC', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'SE', 'SI', 'SK', 'TR', 'UA'],
    'OC': ['AU', 'NZ', 'FJ'],
    'AS': ['AE', 'AF', 'BT', 'CN', 'CY', 'HK', 'ID', 'IL', 'IN', 'IR', 'JO', 'JP', 'KG', 'KH', 'KR', 'KZ', 'LB', 'LY', 'MY', 'PH', 'PK', 'RU', 'SG', 'TH', 'TW'],
    'AF': ['AO', 'CM', 'DZ', 'EG', 'GY', 'JM', 'KE', 'MA', 'NG', 'TN', 'ZA']
}


# Remove unwanted features from Dataframe
def drop_unused_columns(df):
    logger.info('Dropping unused columns')

    return df.drop('homepage', axis=1) \
       .drop('id', axis=1) \
       .drop('keywords', axis=1) \
       .drop('overview', axis=1) \
       .drop('release_date', axis=1) \
       .drop('status', axis=1) \
       .drop('tagline', axis=1) \
       .drop('title', axis=1) \
       .drop('original_title', axis=1) \
       .drop('production_companies', axis=1)


# Split genres into separate columns (e.g. 'genres'-> 'genre_western' and 'genre_comedy')
def normalize_genres(df):
    logger.info("Normalizing column: 'genres'")

    genres = df.loc[:, 'genres']
    genres_normalized = []

    for genre in genres:
        data = json.loads(genre)
        names = list(map(lambda x: x['name'].replace(" ", "_").lower(), data))
        genres_normalized.append(names)


    logger.debug("Creating column: 'genres_normalized'")

    df['genres_normalized'] = genres_normalized

    logger.debug("One-hot encoding column: 'genres_normalized'")

    df1 = (
        df['genres_normalized'].explode()
        .str.get_dummies().groupby(level=0).sum().add_prefix('genres_')
    )

    logger.debug("Dropping columns: 'genres', 'genres_normalized'")

    return df.drop('genres', axis=1).drop('genres_normalized', axis=1).join(df1)


def map_country_to_region(country):
    iso = country['iso_3166_1']

    for item in REGIONS.items():
        region = item[0]
        countries = item[1]

        if iso in countries:
            return region

    return None


# Split production countries into separate columns
def normalize_production_countries(df):
    logger.info("Normalizing column: 'production_countries'")

    production_countries = df.loc[:, 'production_countries']
    production_countries_normalized = []

    for production_country in production_countries:
        data = json.loads(production_country)
        regions = set(map(map_country_to_region, data))
        production_countries_normalized.append(regions)

    
    logger.debug("Creating column: 'production_countries_normalized'")

    df['production_countries_normalized'] = production_countries_normalized

    logger.debug("One-hot encoding column: 'production_countries_normalized'")

    df2 = (
        df['production_countries_normalized'].explode()
        .str.get_dummies().groupby(level=0).sum().add_prefix('region_') # shortened it from production_country to region
    )

    logger.debug("Dropping columns: 'production_countries', 'production_countries_normalized'")

    return df.drop('production_countries', axis=1).drop('production_countries_normalized', axis=1).join(df2)


# Remove movies with 0 or null runtime
def remove_nulls(df):
    logger.info("Dropping null columns: 'runtime', 'budget'")

    df = df.loc[(df[['runtime', 'budget']] != 0).all(axis=1)]
    df = df[df['runtime'].notna()]

    return df


# Create dataframe from CSV file
df = pd.read_csv('tmdb_5000_movies.csv', sep=',')

df = drop_unused_columns(df)
df = normalize_genres(df)
df = normalize_production_countries(df)
df = remove_nulls(df)


df['runtime'] = df['runtime'].apply(lambda x : x - (x % 10))


logger.debug("Saving transformations to 'normalized.csv'")

# Create new modified CSV file for training usage
df.to_csv('normalized.csv')

logger.info("Saved transformations to 'normalized.csv'")


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
