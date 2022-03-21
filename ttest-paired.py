# using scipy
from bioinfokit.analys import get_data, stat
import pandas as pd
df=pd.read_csv("Book1.csv") 
# paired t-test

# load dataset as pandas dataframe
df.head(2)
res = stat()

df
res.ttest(df = df, res = ['Pofcity', 'Numred'], test_type = 3)
print(res.summary)
