from normalize_data import *
import pytest
import pandas as pd


def test_map_country_to_region():
    df = create_examples()
    df2 = transform_production_countries(df)
    
    firstRow = df2['region_NA'].iloc[0]
    assert firstRow == 1
    
def test_normalize_revenue():
    df = create_examples()
    df2 = normalize_revenue(df)

    assert df2['revenue_normalized'].iloc[1] == 0.2703306473829645

def test_normalize_popularity():
    df = create_examples()
    df2 = normalize_popularity(df)

    assert df2['popularity_normalized'].iloc[2] == 0.5957135132357084

def test_normalize_budget():
    df = create_examples()
    df2 = normalize_budget(df)

    assert df2['budget_normalized'].iloc[3] == -0.5200509674923438

def test_remove_nulls():
    df = create_examples()
    df2 = remove_nulls(df)

    assert len(df.columns) == len(df2.columns)

def test_transform_genres():
    df = create_examples()
    df2 = transform_genres(df)

    assert df2['genres_science_fiction'].iloc[4] == 1


def create_examples():
    df = pd.read_csv('testData.csv', sep=',')
    
    return df

# create_examples()
test_normalize_revenue()
test_map_country_to_region()
test_normalize_popularity()
test_normalize_budget()
test_remove_nulls()
test_transform_genres()