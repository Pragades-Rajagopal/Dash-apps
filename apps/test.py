#%%
# import pandas as pd

# d = pd.read_csv('intro_bees.csv')
# d1 = d["State"].unique()
# # d.reset_index(inplace=True)
# print(d1)

 # %%
# import pandas as pd
# d = pd.read_csv('intro_bees.csv')
# d = d.groupby(["State", "Year", "Affected by", "state_code"])[["Pct of Colonies Impacted"]].mean()
# d.reset_index(inplace=True)
# d = d[d["State"].isin(['Virginia', 'Alabama'])]
# d = d[d["Affected by"] == 'Disease']
# print(d)

# %%
# import pandas as pd
# d = pd.read_csv('intro_bees.csv')
# d = d.groupby(["State", "Year", "Affected by", "state_code"])[["Pct of Colonies Impacted"]].mean()
# d.reset_index(inplace=True)

# u = d["Affected by"].unique()
# print(u)
