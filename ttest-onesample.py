from scipy import stats as st
from bioinfokit.analys import get_data
import pandas as pd

df=pd.read_csv("Book1.csv") 
# load dataset as pandas dataframe
df

# t test using scipy
a =  df['size'].to_numpy()
# use parameter "alternative" for two-sided or one-sided test
st.ttest_1samp(a=a, popmean=5)
# output
Ttest_1sampResult(statistic=0.36789006583267403, pvalue=0.714539654336473)