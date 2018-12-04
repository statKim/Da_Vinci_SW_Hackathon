import lightgbm as lgb
import dataEncoding

# load model to predict
# bst = lgb.Booster(model_file='model/model_lotte.txt')

# input 날짜 입력
yea = 2018
mo = 12
da = 9
place = "nam"

X_test = dataEncoding.dataencoding(mo, da, place)["data"]
# y_pred = bst.predict(X_test)
print(X_test)
# print(float(y_pred[0]))
# from datetime import datetime
# now = datetime.now().weekday()
# print(now)