import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# Upload Data
filename = 'weather_ndvi_2016feb_jun.csv'
weather_ndvi_2016 = pd.read_csv(filename)
weather_ndvi_2016 = weather_ndvi_2016.drop(['Unnamed: 0'], axis = 1)

filename = 'weather_ndvi_2017feb_jun.csv'
weather_ndvi_2017 = pd.read_csv(filename)
weather_ndvi_2017 = weather_ndvi_2017.drop(['Unnamed: 0'], axis = 1)

filename = 'weather_ndvi_2018feb_jun.csv'
weather_ndvi_2018 = pd.read_csv(filename)
weather_ndvi_2018 = weather_ndvi_2018.drop(['Unnamed: 0'], axis = 1)



# Define X and y
X = weather_ndvi_2016.drop(['County','Yield 2016','Year'], axis = 1)
y = weather_ndvi_2016[['Yield 2016']]



# Define Train and Test
X_train = weather_ndvi_2016[['Max_Temp','NDVI','Yield 2015']]
y_train = y

X_test = weather_ndvi_2017[['Max_Temp','NDVI','Yield 2016']]
y_test = weather_ndvi_2017[['Yield 2017']]



# Train Random Forest Model
rf = RandomForestRegressor(random_state=55)
rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)

y_pred = np.array(y_pred)
y_pred = y_pred.astype('float64')
y_pred = pd.DataFrame(y_pred)
y_pred= np.array(y_pred)



# Print Metrics
print("R2: {}".format(r2_score(y_test, y_pred)))
print("RMSE: {}".format(np.sqrt(mean_squared_error(y_test, y_pred))))
print("SMAPE: {}".format(100 * (sum(abs(y_test.values-y_pred)/(abs(y_test.values)+abs(y_pred))))/(len(y_test.values))))
print("%bias: {}".format(100 * (sum(y_pred - y_test.values) / sum(y_test.values))))
print("Mean Accuracy: {}".format(sum(1 - abs(y_pred/y_test.values))))



# 2018 Predictions
weather_ndvi_2018 = weather_ndvi_2018.drop(['County'], axis = 1)
X_2018 = weather_ndvi_2018[['Max_PrProb','NDVI','Yield 2017']]

y_pred_2018 = rf.predict(X_2018)
y_pred_2018 = pd.DataFrame(y_pred_2018)

counties= ['Yolo','Fresno','Kern','Merced','Kings','San Joaquin','Solano','Stanislaus']

yield_2018 = pd.DataFrame(columns={'Yield_2018','County'})

yield_2018[['Yield_2018']] = y_pred_2018
yield_2018[['County']]= counties

yield_2018.to_csv('predicted_yield_2018.csv')
