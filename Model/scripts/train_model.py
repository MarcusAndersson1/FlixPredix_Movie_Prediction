import logging
import pandas as pd  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from joblib import dump

MODEL_LOCATION = "models/tmp/model.joblib"

logging.basicConfig(level=logging.INFO) # switch to logging.DEBUG for more info
logger = logging.getLogger('train_model')

logger.info("Loading data from '/data/normalized.csv'")

df = pd.read_csv('data/normalized.csv', sep=',')

X = df[['budget', 'runtime', 
        'genres_action', 'genres_adventure','genres_animation',
        'genres_comedy','genres_crime','genres_documentary',
        'genres_drama','genres_family','genres_fantasy',
        'genres_foreign','genres_history','genres_horror',
        'genres_music','genres_mystery','genres_romance',
        'genres_science_fiction','genres_thriller','genres_tv_movie',
        'genres_war','genres_western','region_AF','region_AS',
        'region_EU','region_NA','region_OC','region_SA','region_UK']].values
y = df['vote_average'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

logger.info('Training linear regression model')

model = LinearRegression()
model.fit(X_train, y_train)

logger.info("Saving model to '{}'".format(MODEL_LOCATION))

dump(model, MODEL_LOCATION)

logger.info("Saved model to '{}'".format(MODEL_LOCATION))
