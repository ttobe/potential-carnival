import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
# 데이터 프레임 전체에 scaling 적용
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error
import numpy as np

# 파일 읽기
path = '../Data/float_ratings.csv'
df = pd.read_csv(path)
df.info()
df_x = df.drop(columns=['rating'])
df_y = df['rating'].values

naver_path = '../Data/results_naver.csv'
df_naver = pd.read_csv(naver_path)
df_naver.info()
from sklearn.preprocessing import StandardScaler
# 스케일링
std = StandardScaler()
std.fit(df_x)
df_x_scaled = std.transform(df_x)
std.fit(df_naver)
df_test_scaled = std.transform(df_naver)
scaler = MinMaxScaler(feature_range=(0, 6))

# 데이터 스케일링
scaled_y = scaler.fit_transform(df_y.reshape(-1, 1))
scaled_y = scaled_y.ravel()
print("---------------")
print(scaled_y)
# df_y.info()
x_train, x_test, y_train, y_test = train_test_split(df_x_scaled, scaled_y, test_size=0.3, random_state=37)


# mms = MinMaxScaler()
# mms.fit(df_x)
# df_x_scaled = mms.transform(df_x)
# print(df_x_scaled)
# x_train, x_test, y_train, y_test = train_test_split(df_x_scaled, df_y, test_size=0.2, random_state=37)

print(x_train.shape , y_train.shape)

# from sklearn.neighbors import KNeighborsClassifier
# for k in range(1, 11):
#     knn = KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
#     knn.fit(x_train, y_train)
#     score = knn.score(x_test, y_test)
#     print('k: %d, accuracy: %.2f' % (k, score*100))


print("---------------")
print("LinearRegression")

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test,pred))
# print("RMSE: ", rmse)
# import joblib
# joblib.dump(model, './model/linear.pkl')
preds = model.predict(df_test_scaled)


# print("---------------")
# print("DecisionTreeClassifier")

# dtc = DecisionTreeClassifier()
# dtc.fit(x_train, y_train)
# # print('모델의 정확도 :', round(dtc.score(x_test, y_test), 4))

# pred = dtc.predict(x_test)
# rmse = np.sqrt(mean_squared_error(y_test,pred))
# print("Rmse: ", rmse)


print("---------------")
print("RandomForestRegressor")

from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor(n_estimators=100)
forest_reg.fit(x_train, y_train)
housing_predictions = forest_reg.predict(x_test)
forest_mse = mean_squared_error(y_test, housing_predictions)
forest_rmse = np.sqrt(forest_mse)
print("Rmse: ", forest_rmse)
preds = forest_reg.predict(df_test_scaled)
print(preds)


import pandas as pd
import xgboost
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import explained_variance_score

print("---------------")
print("XGBRegressor")

xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                           colsample_bytree=1, max_depth=7)
xgb_model.fit(x_train , y_train)
xgboost.plot_importance(xgb_model)
# plt.show()
pred = xgb_model.predict(x_test)

r_sq = xgb_model.score(x_train, y_train)
# print(pred[0])
# print(y_test)
# for i in range(5):
#     print("Predict: % f" %(pred[i]), end=' ')
#     print("Answer: ", y_test[i])

mse = np.sqrt(mean_squared_error(y_test, pred))
print("RMSE : % f" %(mse))
# print("R2 score ",r_sq)
# print(explained_variance_score(pred,y_test))
preds = xgb_model.predict(df_test_scaled)
print(preds)
preds_str = [str(value) for value in preds]
result = ",".join(preds_str)
with open("./predicted.txt", "w") as file:
    file.write(result)