import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
#loading the dataset
happiness_2015 = pd.read_csv("C:/Users/saxen/PycharmProjects/pythonProject/2015.csv")
happiness_2015.columns = ['Country', 'Region', 'Happiness_Rank', 'Happiness_Score',
       'Standard Error', 'Economy', 'Family',
       'Health', 'Freedom', 'Trust',
       'Generosity', 'Dystopia_Residual']
columns_2015 = ['Region', 'Standard Error']
new_dropped_2015 = happiness_2015.drop(columns_2015, axis=1)
happiness_2016 =  pd.read_csv("C:/Users/saxen/PycharmProjects/pythonProject/2016.csv")
columns_2016 = ['Region', 'Lower Confidence Interval','Upper Confidence Interval' ]
dropped_2016 = happiness_2016.drop(columns_2016, axis=1)
dropped_2016.columns = ['Country', 'Happiness_Rank', 'Happiness_Score','Economy', 'Family',
       'Health', 'Freedom', 'Trust',
       'Generosity', 'Dystopia_Residual']
happiness_2017 =  pd.read_csv("C:/Users/saxen/PycharmProjects/pythonProject/2017.csv")
columns_2017 = ['Whisker.high','Whisker.low' ]
dropped_2017 = happiness_2017.drop(columns_2017, axis=1)
dropped_2017.columns = ['Country', 'Happiness_Rank', 'Happiness_Score','Economy', 'Family',
       'Health', 'Freedom', 'Trust',
       'Generosity', 'Dystopia_Residual']
happiness_2018=pd.read_csv('C:/Users/saxen/PycharmProjects/pythonProject/2018.CSV')
Trust = happiness_2018.iloc[:,8]
happiness_2018 = happiness_2018.drop(happiness_2018.columns[8],axis=1)
happiness_2018.insert(7,'Trust',Trust)
happiness_2018.columns = ['Happiness_Rank','Country','Happiness_Score','Economy','Family','Health','Freedom','Trust','Generosity']
happiness_2019=pd.read_csv('C:/Users/saxen/PycharmProjects/pythonProject/2019.csv')
Trust = happiness_2019.iloc[:,8]
happiness_2019=happiness_2019.drop(happiness_2019.columns[8],axis=1)
happiness_2019.insert(7,'Trust',Trust)
happiness_2019.columns = ['Happiness_Rank','Country','Happiness_Score','Economy','Family','Health','Freedom','Trust','Generosity']
frames = [new_dropped_2015, dropped_2016, dropped_2017,happiness_2018,happiness_2019]
happiness = pd.concat(frames)
print(happiness.head())
print(happiness.describe())
dropped_happy = happiness.drop(["Country", "Happiness_Rank"], axis=1)
dropped_happy=dropped_happy.dropna()

from sklearn.linear_model import LinearRegression
X = dropped_happy.drop("Happiness_Score", axis = 1)
lm = LinearRegression()
model=lm.fit(X, dropped_happy.Happiness_Score)

print("Estimated Intercept is", lm.intercept_)
print("The number of coefficients in this model are", lm.coef_)

# saving the model
import pickle
pickle_out = open("regression.pkl", mode = "wb")
pickle.dump(model, pickle_out)
pickle_out.close()
