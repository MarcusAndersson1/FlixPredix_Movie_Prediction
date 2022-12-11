import logging
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from joblib import load

MODEL_LOCATION = "models/tmp/model.joblib"

logging.basicConfig(level=logging.INFO) # switch to logging.DEBUG for more info
logger = logging.getLogger('test_model')

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

logger.info("Loading model from '{}'".format(MODEL_LOCATION))

model = load(MODEL_LOCATION)

logger.info("Loaded model from '{}'".format(MODEL_LOCATION))
logger.info('Creating prediction set')

y_pred = model.predict(X_test)

predictions = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

logger.info("Saving predictions to '/data/predictions.csv'")

predictions.to_csv('data/predictions.csv')

logger.info("Saved predictions to '/data/predictions.csv'")

entries = np.arange(0, len(predictions), 1)

plt.plot(entries, y_test.flatten(), entries, y_pred.flatten())
plt.xlabel('Entries')
plt.ylabel('Actual vs Predicted')
plt.legend(['Actual', 'Predicted'])
plt.show()