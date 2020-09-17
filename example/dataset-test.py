#%%
import pandas as pd
data = pd.read_csv('emission-data.csv')
data = data.groupby(['Country', 'Continent'])[['Emission']].mean()
# a = data[data['Country'] == 'Afghanistan'].mean()
# a
data.reset_index(inplace=True)

c = data[data['Country'] == 'Trinidad And Tobago']
c
# %%
