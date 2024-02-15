import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
unique_values = data['whoAmI'].unique()
one_hot_df = pd.concat([data['whoAmI'].eq(value).astype(int) for value in unique_values], axis=1)
one_hot_df.columns = unique_values
print(one_hot_df.head())
