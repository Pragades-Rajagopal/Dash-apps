#%%
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/flightdata.csv')
pd.set_option('display.max_columns', 31)


# %%
df.drop(columns=['Unnamed: 0','month', 'day','carrier',
       'flight', 'tailnum', 'origin', 'dest','time_hour', 'flightb','airport', 'lat', 'lon', 'alt', 'tz', 'dst', 'tzone'], inplace=True)
# %%
# df.head(5)
# %%
# df.isnull().sum()
# %%
# df.isna().sum()
# %%
import numpy as np
cols = ['dep_time','dep_delay','arr_time','arr_delay','air_time','avgdelay']

for i in cols:
    df[i] = df[i].replace(0, np.nan)
    m = float(df[i].mean(skipna=True))
    df[i] = df[i].replace(np.nan, m)
# %%
data = df.copy()
# %%
# data.columns
# %%
# a = data[data["airline"] == "American Airlines Inc."]
# a