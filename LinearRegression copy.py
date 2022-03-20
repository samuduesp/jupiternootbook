import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("regression.csv")
df

df.describe()


################ need to change x and y axis ###################

plt.scatter(df.Pofcity,df.Numred,color='red') #Scatterplot

df.hist() #Histogram

##### R value #########
df.corr() #Finding the Coefficient of Correlation (r)

sns.heatmap(df.corr(),annot=True,vmin=-1,vmax=-1)

df.isna().sum() # find missing values

#Assign Features to X and Y
x=df.iloc[:,0:1] 
x.head(1)

y=df.iloc[:,1:]
y.head(1)

plt.scatter(x, y)
plt.show()

# Model Building with sklearn

from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)

plt.scatter(x,y)
plt.plot(x,lin_reg.predict(x),color='green')
plt.title("Regression Model")

# m (slope) and c(intercept) values
lin_reg.coef_ # m value 
lin_reg.intercept_ # c value - intercept