import numpy as np
import pandas as pd
import json
import logging
import csv_to_sqlite 


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
def transform_genres(df):
    logger.info("Transforming column: 'genres'")

    genres = df.loc[:, 'genres']
    genres_transformed = []

    for genre in genres:
        data = json.loads(genre)
        names = list(map(lambda x: x['name'].replace(" ", "_").lower(), data))
        genres_transformed.append(names)


    logger.debug("Creating column: 'genres_transformed'")

    df['genres_transformed'] = genres_transformed

    logger.debug("One-hot encoding column: 'genres_transformed'")

    df1 = (
        df['genres_transformed'].explode()
        .str.get_dummies().groupby(level=0).sum().add_prefix('genres_')
    )

    logger.debug("Dropping columns: 'genres', 'genres_transformed'")

    return df.drop('genres', axis=1).drop('genres_transformed', axis=1).join(df1)


def map_country_to_region(country):
    iso = country['iso_3166_1']

    for item in REGIONS.items():
        region = item[0]
        countries = item[1]

        if iso in countries:
            return region

    return None


# Split production countries into separate columns
def transform_production_countries(df):
    logger.info("Transforming column: 'production_countries'")

    production_countries = df.loc[:, 'production_countries']
    production_countries_transformed = []

    for production_country in production_countries:
        data = json.loads(production_country)
        regions = set(map(map_country_to_region, data))
        production_countries_transformed.append(regions)

    
    logger.debug("Creating column: 'production_countries_transformed'")

    df['production_countries_transformed'] = production_countries_transformed

    logger.debug("One-hot encoding column: 'production_countries_transformed'")

    df2 = (
        df['production_countries_transformed'].explode()
        .str.get_dummies().groupby(level=0).sum().add_prefix('region_') # shortened it from production_country to region
    )

    logger.debug("Dropping columns: 'production_countries', 'production_countries_transformed'")

    return df.drop('production_countries', axis=1).drop('production_countries_transformed', axis=1).join(df2)


def normalize_popularity(df):
    logger.info("Normalizing column: 'popularity'")

    normalized_popularity = (df['popularity'] - df['popularity'].min()) / (df['popularity'].max() - df['popularity'].min())

    df['popularity_normalized'] = normalized_popularity

    col = df.pop('popularity_normalized')
    df.insert(df.columns.get_loc('popularity') + 1, 'popularity_normalized', col)

    return df


def normalize_revenue(df):
    logger.info("Normalizing column: 'revenue'")

    normalized_revenue = (df['revenue'] - df['revenue'].min()) / (df['revenue'].max() - df['revenue'].min())

    df['revenue_normalized'] = normalized_revenue

    col = df.pop('revenue_normalized')
    df.insert(df.columns.get_loc('revenue') + 1, 'revenue_normalized', col)

    return df


def normalize_budget(df):
    logger.info("Normalizing column: 'budget'")

    # normalized_budget = (df['budget'] - df['budget'].min()) / (df['budget'].max() - df['budget'].min())
    normalized_budget = (df['budget'] - df['budget'].mean()) / df['budget'].std()

    df['budget_normalized'] = normalized_budget

    col = df.pop('budget_normalized')
    df.insert(df.columns.get_loc('budget') + 1, 'budget_normalized', col)

    return df


# Remove movies with 0 or null runtime
def remove_nulls(df):
    logger.info("Dropping null columns: 'runtime', 'budget', 'vote_count'")

    df = df.loc[(df[['runtime', 'budget']] != 0).all(axis=1)]
    df = df[df['runtime'].notna()]
    df = df.loc[(df[['vote_count']] >= 10).all(axis=1)]

    return df

if __name__ == "__main__":
    # Create dataframe from CSV file
    df = pd.read_csv('data/tmdb_5000_movies.csv', sep=',')

    df = drop_unused_columns(df)
    df = transform_genres(df)
    df = transform_production_countries(df)
    df = normalize_popularity(df)
    df = normalize_revenue(df)
    df = normalize_budget(df)
    df = remove_nulls(df)


    logger.debug("Saving transformations to '/data/normalized.csv'")

    # Create new modified CSV file for training usage
    df.to_csv('data/normalized.csv')

    logger.info("Saved transformations to '/data/normalized.csv'")

    logger.info("Saving transformations to '/data/normalized.db'")

    csv_to_sqlite.write_csv(["data/normalized.csv"], "data/normalized.db", csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250"))

    logger.info("Saved transformations to '/data/normalized.db'")

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
