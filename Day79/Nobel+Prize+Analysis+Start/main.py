import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('nobel_prize_data.csv')

# What is the shape of `df_data`? How many rows and columns?
print(df_data.shape)
# (962, 16)

# What are the column names?
print(df_data.columns)
# Index(['year', 'category', 'prize', 'motivation', 'prize_share',
#        'laureate_type', 'full_name', 'birth_date', 'birth_city',
#        'birth_country', 'birth_country_current', 'sex', 'organization_name',
#        'organization_city', 'organization_country', 'ISO'],
#       dtype='object')

# In which year was the Nobel prize first awarded?
# Which year is the latest year included in the dataset?
print(df_data.head())
print(df_data.sort_values("year", ascending=True).head())
#    year    category                                           prize                                         motivation prize_share  ...   sex   organization_name organization_city organization_country  ISO
# 0  1901   Chemistry               The Nobel Prize in Chemistry 1901  "in recognition of the extraordinary services ...         1/1  ...  Male   Berlin University            Berlin              Germany  NLD
# 1  1901  Literature              The Nobel Prize in Literature 1901  "in special recognition of his poetic composit...         1/1  ...  Male                 NaN               NaN                  NaN  FRA
# 2  1901    Medicine  The Nobel Prize in Physiology or Medicine 1901  "for his work on serum therapy, especially its...         1/1  ...  Male  Marburg University           Marburg              Germany  POL
# 3  1901       Peace                      The Nobel Peace Prize 1901                                                NaN         1/2  ...  Male                 NaN               NaN                  NaN  FRA
# 4  1901       Peace                      The Nobel Peace Prize 1901                                                NaN         1/2  ...  Male                 NaN               NaN                  NaN  CHE

# [5 rows x 16 columns]
# Which year is the latest year included in the dataset?
print(df_data.sort_values("year", ascending=False).head(1))
#      year category                            prize                                         motivation prize_share laureate_type  ... birth_country_current   sex     organization_name organization_city organization_country ISO
# 961  2020  Physics  The Nobel Prize in Physics 2020  “for the discovery that black hole formation i...         1/2    Individual  ...        United Kingdom  Male  University of Oxford            Oxford       United Kingdom GBR

# [1 rows x 16 columns]

# Are there any duplicate values in the dataset?
print(df_data.duplicated().values.any())
# False

# Are there NaN values in the dataset?
print(df_data.isna().values.any())
# True

# Which columns tend to have NaN values?
print(df_data.columns[df_data.isna().any()].tolist())
# ['motivation', 'birth_date', 'birth_city', 'birth_country', 'birth_country_current', 'sex', 'organization_name', 'organization_city', 'organization_country', 'ISO']

# How many NaN values are there per column?
nan_counts = df_data.isna().sum()
print(nan_counts)
# year                       0
# category                   0
# prize                      0
# motivation                88
# prize_share                0
# laureate_type              0
# full_name                  0
# birth_date                28
# birth_city                31
# birth_country             28
# birth_country_current     28
# sex                       28
# organization_name        255
# organization_city        255
# organization_country     254
# ISO                       28
# dtype: int64
# Why do these columns have NaN values?


col_subset = ['year','category', 'laureate_type', 'birth_date','full_name', 'organization_name']
print(df_data.loc[df_data.birth_date.isna()][col_subset].head())
#      year category laureate_type birth_date                                          full_name organization_name
# 24   1904    Peace  Organization        NaN  Institut de droit international (Institute of ...               NaN
# 60   1910    Peace  Organization        NaN  Bureau international permanent de la Paix (Per...               NaN
# 89   1917    Peace  Organization        NaN  Comité international de la Croix Rouge (Intern...               NaN
# 200  1938    Peace  Organization        NaN  Office international Nansen pour les Réfugiés ...               NaN
# 215  1944    Peace  Organization        NaN  Comité international de la Croix Rouge (Intern...               NaN

print(df_data.loc[df_data.organization_name.isna()][col_subset].head())
#    year    category laureate_type  birth_date                           full_name organization_name
# 1  1901  Literature    Individual  1839-03-16                     Sully Prudhomme               NaN
# 3  1901       Peace    Individual  1822-05-20                      Frédéric Passy               NaN
# 4  1901       Peace    Individual  1828-05-08                   Jean Henry Dunant               NaN
# 7  1902  Literature    Individual  1817-11-30  Christian Matthias Theodor Mommsen               NaN
# 9  1902       Peace    Individual  1843-05-21                Charles Albert Gobat               NaN

# Convert the `birth_date` column to Pandas `Datetime` objects
df_data.birth_date = pd.to_datetime(df_data.birth_date)

# Add a Column called `share_pct` which has the laureates' share as a percentage in the form of a floating-point number.
separated_values = df_data.prize_share.str.split('/', expand=True)
# print(separated_values[0])
# print(separated_values[1])
numerator = pd.to_numeric(separated_values[0])
denomenator = pd.to_numeric(separated_values[1])
# separated_values[1]
value = numerator / denomenator
df_data["share_pct"] = value*100
print(df_data.share_pct.head())
# 0   100.00
# 1   100.00
# 2   100.00
# 3    50.00
# 4    50.00
# Name: share_pct, dtype: float64
print(df_data.head())
#    year    category                                           prize                                         motivation prize_share  ...   organization_name organization_city organization_country  ISO share_pct
# 0  1901   Chemistry               The Nobel Prize in Chemistry 1901  "in recognition of the extraordinary services ...         1/1  ...   Berlin University            Berlin              Germany  NLD    100.00
# 1  1901  Literature              The Nobel Prize in Literature 1901  "in special recognition of his poetic composit...         1/1  ...                 NaN               NaN                  NaN  FRA    100.00
# 2  1901    Medicine  The Nobel Prize in Physiology or Medicine 1901  "for his work on serum therapy, especially its...         1/1  ...  Marburg University           Marburg              Germany  POL    100.00
# 3  1901       Peace                      The Nobel Peace Prize 1901                                                NaN         1/2  ...                 NaN               NaN                  NaN  FRA     50.00
# 4  1901       Peace                      The Nobel Peace Prize 1901                                                NaN         1/2  ...                 NaN               NaN                  NaN  CHE     50.00

# [5 rows x 17 columns]
print(df_data.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 962 entries, 0 to 961
# Data columns (total 17 columns):
#  #   Column                 Non-Null Count  Dtype
# ---  ------                 --------------  -----
#  0   year                   962 non-null    int64
#  1   category               962 non-null    object
#  2   prize                  962 non-null    object
#  3   motivation             874 non-null    object
#  4   prize_share            962 non-null    object
#  5   laureate_type          962 non-null    object
#  6   full_name              962 non-null    object
#  7   birth_date             934 non-null    datetime64[ns]
#  8   birth_city             931 non-null    object
#  9   birth_country          934 non-null    object
#  10  birth_country_current  934 non-null    object
#  11  sex                    934 non-null    object
#  12  organization_name      707 non-null    object
#  13  organization_city      707 non-null    object
#  14  organization_country   708 non-null    object
#  15  ISO                    934 non-null    object
#  16  share_pct              962 non-null    float64
# dtypes: datetime64[ns](1), float64(1), int64(1), object(14)
# memory usage: 127.9+ KB
# None


