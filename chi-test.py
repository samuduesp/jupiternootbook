import numpy as np
import pandas as pd
from bioinfokit.analys import stat, get_data

#df = get_data('drugdata').data
df=pd.read_csv("chi.csv")
df

# set treatments column as index
df = df.set_index('treatments')
# output
df.head()
# run chi-square test for independence
res = stat()
res.chisq(df = df)
# output
print(res.summary)
print(res.expected_df)