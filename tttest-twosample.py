# using scipy
from scipy import stats as st
from bioinfokit.analys import get_data
import pandas as pd

df= pd.read_csv("Book1.csv") 

a = df['Pofcity'].to_numpy()
b = df['Numred'].to_numpy()
st.ttest_ind(a = a, b = b, equal_var = True)