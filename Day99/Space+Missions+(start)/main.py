import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# These might be helpful:
# from iso3166 import countries
import iso3166
from datetime import datetime, timedelta

import rich

pd.options.display.float_format = '{:,.2f}'.format

df_data = pd.read_csv('mission_launches.csv')

# What is the shape of `df_data`?
# How many rows and columns does it have?
print(df_data.shape)
# (4324, 9)
# 4324 rows
# 9 columns

# What are the column names?
rich.print(df_data.columns)
# Index(['Unnamed: 0.1', 'Unnamed: 0', 'Organisation', 'Location', 'Date', 'Detail', 'Rocket_Status', 'Price', 'Mission_Status'], dtype='object')

# Are there any NaN values or duplicates?
print(df_data.isna().values.any())
# True

# Consider removing columns containing junk data.
df_data_clean = df_data.dropna()
print(df_data_clean.isna().values.any())
# False

# Create a chart that shows the number of space mission launches by organisation.
import plotly.express as px
import plotly.io as pio
ratings = df_data_clean.Organisation.value_counts()
print(ratings)
# CASC               158
# NASA               149
# SpaceX              99
# ULA                 98
# Arianespace         96
# Northrop            83
# ISRO                67
# MHI                 37
# VKS RF              33
# US Air Force        26
# Roscosmos           23
# Kosmotras           22
# ILS                 13
# Eurockot            13
# Rocket Lab          13
# Martin Marietta      9
# Lockheed             8
# Boeing               7
# JAXA                 3
# RVSN USSR            2
# Sandia               1
# Virgin Orbit         1
# ESA                  1
# ExPace               1
# EER                  1
# Name: Organisation, dtype: int64
fig = px.pie(
    labels=ratings.index,
    values=ratings.values,
    title="Organisation",
    names=ratings.index,
)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

# fig = plt.pie(
#     x= ratings.values,
#     labels=ratings.index,
#     autopct='%.1f%%'
# )
# plt.update_traces()
# plt.show()


# Number of Active versus Retired Rockets
# How many rockets are active compared to those that are decomissioned?
rocket_status = df_data_clean.Rocket_Status.value_counts()
print(rocket_status)
# StatusActive     586
# StatusRetired    378
# Name: Rocket_Status, dtype: int64

# Distribution of Mission Status
# How many missions were successful?
# How many missions failed?
mission_status = df_data_clean.Mission_Status.value_counts()
print(mission_status)
# Success              910
# Failure               36
# Partial Failure       17
# Prelaunch Failure      1
# Name: Mission_Status, dtype: int64

# How Expensive are the Launches?
# Create a histogram and visualise the distribution. The price column is given in USD millions (careful of missing values).
launch_price = df_data_clean.Price.value_counts()
print(launch_price)
# 450.0      136
# 200.0       75
# 40.0        55
# 62.0        41
# 30.8        38
# 109.0       37
# 50.0        34
# 64.68       34
# 29.75       33
# 90.0        32
# 41.8        31
# 48.5        26
# 29.15       25
# 31.0        22
# 29.0        22
# 59.0        22
# 69.7        17
# 21.0        16
# 65.0        16
# 35.0        16
# 56.5        15
# 37.0        15
# 164.0       15
# 7.5         14
# 1,160.0     13
# 47.0        13
# 25.0        12
# 350.0       11
# 153.0       11
# 45.0        10
# 112.5        9
# 5.3          9
# 123.0        8
# 145.0        7
# 85.0         7
# 120.0        7
# 80.0         7
# 115.0        6
# 59.5         5
# 7.0          5
# 46.0         5
# 136.6        4
# 63.23        4
# 140.0        3
# 133.0        3
# 190.0        3
# 130.0        3
# 135.0        2
# 5,000.0      2
# 39.0         2
# 55.0         1
# 15.0         1
# 20.14        1
# 20.0         1
# 12.0         1
# 28.3         1
# Name: Price, dtype: int64
# TODO: uncompleted
plt.hist(launch_price, color='skyblue', edgecolor='black')
# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Show plot
# plt.close()
# plt.show()



# Use a Choropleth Map to Show the Number of Launches by Country
# Create a choropleth map using [the plotly documentation]
# Experiment with [plotly's available colours]. I quite like the sequential colour `matter` on this map.
# You'll need to extract a `country` feature as well as change the country names that no longer exist.
# separated_values = df_data.prize_share.str.split('/', expand=True)
def country_to_alpha3(country_name):
    if country_name == "New Mexico":
        return "USA"
    elif country_name == "Pacific Missile Range Facility":
        return "USA"
    elif country_name == "Gran Canaria":
        return "USA"
    elif country_name == "Yellow Sea":
        return "CHN"
    elif country_name == "Shahrud Missile Test Site":
        return "IRN"
    elif country_name == "Barents Sea":
        return "RUS" # Russian Federation
    else:
        try:
            country = iso3166.countries.get(country_name)
            alpha3 = country.alpha3
            return alpha3
        except KeyError:
            return None

# df_data_clean["Country"] = df_data_clean.Location.str.split(', ', expand=True)
# df_data_clean["Country"] = df_data_clean.Location.str.split(', ')[-1]
df_data_clean["Country"] = df_data_clean.Location.apply(lambda x: x.split(', ')[-1])
df_data_clean["Country"] = df_data_clean.Location.apply(lambda x: country_to_alpha3(x.split(', ')[-1]))
print(df_data_clean.head())
#    Unnamed: 0.1  Unnamed: 0 Organisation                                           Location                        Date                                             Detail Rocket_Status  Price Mission_Status Country
# 0             0           0       SpaceX         LC-39A, Kennedy Space Center, Florida, USA  Fri Aug 07, 2020 05:12 UTC       Falcon 9 Block 5 | Starlink V1 L9 & BlackSky  StatusActive   50.0        Success     USA
# 1             1           1         CASC  Site 9401 (SLS-2), Jiuquan Satellite Launch Ce...  Thu Aug 06, 2020 04:01 UTC                Long March 2D | Gaofen-9 04 & Q-SAT  StatusActive  29.75        Success     CHN
# 3             3           3    Roscosmos       Site 200/39, Baikonur Cosmodrome, Kazakhstan  Thu Jul 30, 2020 21:25 UTC       Proton-M/Briz-M | Ekspress-80 & Ekspress-103  StatusActive   65.0        Success     KAZ
# 4             4           4          ULA           SLC-41, Cape Canaveral AFS, Florida, USA  Thu Jul 30, 2020 11:50 UTC                         Atlas V 541 | Perseverance  StatusActive  145.0        Success     USA
# 5             5           5         CASC       LC-9, Taiyuan Satellite Launch Center, China  Sat Jul 25, 2020 03:13 UTC  Long March 4B | Ziyuan-3 03, Apocalypse-10 & N...  StatusActive  64.68        Success     CHN
df_countries = df_data_clean.loc[df_data_clean["Mission_Status"] == "Success"][['Unnamed: 0', 'Country']].groupby(['Country']).count().reset_index()
# df_countries = df_data_clean.loc[df_data_clean["Mission_Status"] == "Success"].groupby(['Country']).size().reset_index(name='Count')
print(df_countries.head(5))
#   Country  Unnamed: 0
# 0     CHN         152
# 1     FRA          92
# 2     IND          59
# 3     JPN          40
# 4     KAZ          43
world_map = px.choropleth(
    df_countries,
    locations='Country',
    color='Unnamed: 0',
    color_continuous_scale=px.colors.sequential.matter
)
world_map.update_layout(coloraxis_showscale=True,)
world_map.show()

failure_statuses = ["Failure", "Partial Failure", "Prelaunch Failure"]
df_failures = df_data_clean.loc[df_data_clean["Mission_Status"].isin(failure_statuses)][['Unnamed: 0', 'Country']].groupby(['Country']).count().reset_index()
# print(df_failures.head(5))
print(df_failures)
#   Country  Unnamed: 0
# 0     CHN           7
# 1     FRA           3
# 2     IND           8
# 3     KAZ           3
# 4     NZL           2
# 5     USA          28
world_map = px.choropleth(
    df_failures,
    locations='Country',
    color='Unnamed: 0',
    color_continuous_scale=px.colors.sequential.matter
)
world_map.update_layout(coloraxis_showscale=True,)
world_map.show()

# Create a Plotly Sunburst Chart of the countries, organisations, and mission status.
country_org_status = df_data_clean.groupby(by=['Country','Organisation','Mission_Status'], as_index=False).agg({'Price': pd.Series.count})
country_org_status = country_org_status.sort_values('Price', ascending=False)
burst = px.sunburst(
    country_org_status,
    path=['Country', 'Organisation', 'Mission_Status'],
    values='Price',
    title='Where do Discoveries Take Place?',
)
burst.show()

# Analyse the Total Amount of Money Spent by Organisation on Space Missions
df_data_clean['Price'] = df_data_clean['Price'].str.replace(',', "")
df_data_clean['Price'] = pd.to_numeric(df_data_clean['Price'])
total_spending_by_organisation = df_data_clean.groupby(['Organisation'])['Price'].agg('sum')
print(total_spending_by_organisation)
# Organisation
# Arianespace       16,345.00
# Boeing             1,241.00
# CASC               6,340.26
# EER                   20.00
# ESA                   37.00
# Eurockot             543.40
# ExPace                28.30
# ILS                1,320.00
# ISRO               2,177.00
# JAXA                 168.00
# Kosmotras            638.00
# Lockheed             280.00
# MHI                3,532.50
# Martin Marietta      721.40
# NASA              76,280.00
# Northrop           3,930.00
# RVSN USSR         10,000.00
# Rocket Lab            97.50
# Roscosmos          1,187.50
# Sandia                15.00
# SpaceX             5,444.00
# ULA               14,798.00
# US Air Force       1,550.92
# VKS RF             1,548.90
# Virgin Orbit          12.00
# Name: Price, dtype: float64


# Analyse the Amount of Money Spent by Organisation per Launch
per_spending_by_organisation = df_data_clean.groupby(['Organisation'])['Price'].agg('mean')
print(per_spending_by_organisation.head())
# Organisation
# Arianespace   170.26
# Boeing        177.29
# CASC           40.13
# EER            20.00
# ESA            37.00
# Name: Price, dtype: float64

# Chart the Number of Launches per Year
df_data_clean['Year'] = df_data_clean['Date'].str.split(', ').str[1]
df_data_clean['Year'] = df_data_clean['Year'].str.split(' ').str[0]
print(df_data_clean['Year'].head())
# 0    2020
# 1    2020
# 3    2020
# 4    2020
# 5    2020
# Name: Year, dtype: object
# df_data_clean['Year'] = df_data_clean['Date'].str.split(', ')
# print(df_data_clean['Year'])

count_per_year  = df_data_clean.groupby(['Year']).count().Organisation
print(count_per_year.head())
# Year
# 1964     2
# 1965     2
# 1966     3
# 1967     8
# 1968    10
# Name: Organisation, dtype: int64
plt.figure(figsize=(8,4), dpi=200)
plt.title('Number of Launches per Year', fontsize=9)
plt.yticks(fontsize=7)
plt.xticks(
    # ticks=np.arange(1964, 2021, step=1),
    fontsize=6,
    rotation=45
)
ax = plt.gca() # get current axis
# ax.set_xlim(1964, 2020)
# blue dot
plt.scatter(
    x=count_per_year.index,
    y=count_per_year.values,
    c='dodgerblue',
    alpha=0.7,
    s=100,
)
# red line
plt.plot(
    count_per_year.index,
    count_per_year.values,
    c='crimson',
    linewidth=3,
)
plt.show()

# Chart the Number of Launches Month-on-Month until the Present
moving_average = count_per_year.rolling(window=5).mean()
moving_average.head()
plt.figure(figsize=(8,4), dpi=200)
plt.plot(moving_average.index, moving_average.values, color="red")
plt.show()

# How has the Launch Price varied Over Time?
avg_price_per_year  = df_data_clean.groupby(['Year']).count().Price
print(avg_price_per_year.head())
# Year
# 1964    63.23
# 1965    63.23
# 1966    59.00
# 1967   196.62
# 1968   279.20
# Name: Price, dtype: float64
plt.figure(figsize=(8,4), dpi=200)
plt.title('Price varied per Year', fontsize=9)
plt.yticks(fontsize=7)
plt.xticks(
    # ticks=np.arange(1964, 2021, step=1),
    fontsize=6,
    rotation=45
)
ax = plt.gca() # get current axis
# red line
plt.plot(
    avg_price_per_year.index,
    avg_price_per_year.values,
    c='crimson',
    linewidth=3,
)
plt.show()
