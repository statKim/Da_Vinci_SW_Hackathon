import lightgbm as lgb
import pandas as pd
# import numpy as np
# from sklearn.metrics import mean_squared_error
import test

print('Loading model to predict...')
# load model to predict
bst = lgb.Booster(model_file='model/model_lotte.txt')
# can only predict with the best iteration (or the saving iteration)
#

# input 날짜 입력
yea = 2018
mo = 12
da = 2
place = "nam"

X_test = test.dataencoding(yea, mo, da, place)
y_pred = bst.predict(X_test)
# eval with loaded model
print(float(y_pred[0]))
# pd.DataFrame(y_pred).describe()
