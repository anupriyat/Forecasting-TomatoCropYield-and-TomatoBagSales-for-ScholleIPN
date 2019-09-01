# Forecasting-TomatoCropYield-and-TomatoBagSales-for-ScholleIPN
Forecasting Tomato Bag Quantity Using Predicted Tomato Yield on the Basis of NDVI Values and Weather-Related Variables

# Summary
Scholle IPN’s current demand forecasting methods only consider the quantity of bags sold in the previous year leading to overstocking. The proposed solution is to predict the tomato yield on the basis of weather data, NDVI values, and previous year’s yield and use it to forecast the tomato bag demand more accurately. The solution is built using two models: (1) random forest regressor to estimate annual tomato yield, and (2) linear regression to model the tomato bag sales. The most important weather measurement in predicting tomato yield is maximum temperature. Using the predicted tomato yield improves the forecast accuracy by 2.75%.

Keywords: Tomato, Scholle IPN, NDVI, Temperature, Crop Yield, Cross-sectional, Linear Regression, Random Forest, Ensemble Model

# Weather Visualization 

![Alt text](Fresno_WeatherEDA.png?raw=true "Fresno_WeatherEDA.png")
 
# Modelling Framework
 
![Alt text](ModellingFramework.png?raw=true "ModellingFramework.png")
  
# Predictions
  
![Alt text](Forecast.png?raw=true "Forecast.png")
