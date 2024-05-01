import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from datetime import datetime, timedelta


pd.options.display.float_format = '{:,.2f}'.format

df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")


# What is the shape of the DataFrames?
# How many rows and columns do they have?
print(df_hh_income.shape)        # (29322, 3)
print(df_pct_poverty.shape)      # (29329, 3)
print(df_pct_completed_hs.shape) # (29329, 3)
print(df_share_race_city.shape)  # (29268, 7)
print(df_fatalities.shape)       # (2535, 14)

# What are the column names?
print(df_hh_income.columns)
print(df_pct_poverty.columns)
print(df_pct_completed_hs.columns)
print(df_share_race_city.columns)
print(df_fatalities.columns)

# Are there any NaN values or duplicates?
print(df_hh_income.isna().values.any())        # True
print(df_pct_poverty.isna().values.any())      # False
print(df_pct_completed_hs.isna().values.any()) # False
print(df_share_race_city.isna().values.any())  # False
print(df_fatalities.isna().values.any())       # True

# Consider how to deal with the NaN values. Perhaps substituting 0 is appropriate.
df_hh_income_clean        = df_hh_income.fillna(0)
df_pct_poverty_clean      = df_pct_poverty.fillna(0)
df_pct_completed_hs_clean = df_pct_completed_hs.fillna(0)
df_share_race_city_clean  = df_share_race_city.fillna(0)
df_fatalities_clean       = df_fatalities.fillna(0)





