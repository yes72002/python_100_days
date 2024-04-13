import pandas as pd



sets = pd.read_csv('data/sets.csv')
sets.head()

# In which year were the first LEGO sets released and what were these sets called?
sets.sort_values('year') # A: 1949

# How many different products did the LEGO company sell in their first year of operation?
sets.groupby('year').count() # 5
# or
# sets[sets['year']==1949]

# What are the top 5 LEGO sets with the most number of parts?
sets.sort_values('num_parts', ascending=False).head()

sets.groupby('year').count()

# sets_by_year = sets.sort_values('year', ascending=False)
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()



import matplotlib.pyplot as plt
sets_by_year.tail()

sets_by_year = sets_by_year[:-2]
sets_by_year.tail()
plt.plot(sets_by_year.index, sets_by_year.theme_id, label='theme_id')
plt.xlabel('year')
plt.ylabel('theme_id')
plt.title('theme_id')
plt.legend()
# plt.show(block=False)

# themes_by_year = sets.groupby('year').agg({'theme_id':pd.Series.unique})
# # set_df.groupby("year").agg({"theme_id": "nunique"})
themes_by_year = sets.groupby('year')['theme_id'].nunique()
themes_by_year

# themes_by_year.rename(columns = {'theme_id':'nr_themes'}, inplace = True)
# themes_by_year.rename(columns={'theme_id': 'unique_theme_ids'}, inplace=True)
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df.rename(columns={"A": "a", "B": "c"})
print(type(df))       # <class 'pandas.core.frame.DataFrame'>
print(type(themes_by_year)) # <class 'pandas.core.series.Series'>
# themes_by_year = themes_by_year.to_frame().reset_index()
themes_by_year = themes_by_year.to_frame()
# themes_by_year.to_frame()
print(type(themes_by_year)) # <class 'pandas.core.series.Series'>
themes_by_year.rename(columns={"theme_id": "nr_themes"})
themes_by_year


themes_by_year = themes_by_year[:-2]
print(f"sets_by_year = {sets_by_year}")
print(f"sets_by_year = {sets_by_year.columns}")
print(f"sets_by_year = {sets_by_year['set_num']}")
# plt.plot(themes_by_year.index, themes_by_year.nr_themes)
# plt.plot(themes_by_year.index, themes_by_year.theme_id)
# plt.plot(sets_by_year.index, sets_by_year.set_num)
plt.plot(sets_by_year.index, sets_by_year['set_num'])