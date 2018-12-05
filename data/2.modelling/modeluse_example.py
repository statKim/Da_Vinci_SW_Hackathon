import lightgbm as lgb
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

print('Loading model to predict...')
# load model to predict
bst = lgb.Booster(model_file='model_lotte.txt')
# can only predict with the best iteration (or the saving iteration)

path = "c:/Users/Jiwan/Desktop/Hackathon/"
lotte = pd.read_csv(path+'lotte.csv')
X_test = lotte.iloc[:,3:]

y_pred = bst.predict(X_test)
# eval with loaded model
print(y_pred)
pd.DataFrame(y_pred).describe()
