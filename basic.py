import pandas as pd
import numpy as np

df = pd.read_csv ('mean.csv') 

# print the data set in jupiter notebook
df

# change the colume name you need to get the mean and median
df['Pofcity'].mean()
df['Pofcity'].median()
## stander deviation 
df['Pofcity'].std()

##  Variance  
df['Pofcity'].var() 


## max and min
df['Pofcity'].min()
df['Pofcity'].max()

