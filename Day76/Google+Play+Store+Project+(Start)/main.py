import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# These might be helpful:
from iso3166 import countries
from datetime import datetime, timedelta

pd.options.display.float_format = '{:,.2f}'.format

df_apps = pd.read_csv('apps.csv')

# How many rows and columns does `df_apps` have?
print(df_apps.shape)
# (10841, 12)

# What are the column names?
print(df_apps.columns)
# Index(['App', 'Category', 'Rating', 'Reviews', 'Size_MBs', 'Installs', 'Type', 'Price', 'Content_Rating', 'Genres', 'Last_Updated', 'Android_Ver'], dtype='object')

# Look at a random sample of 5 different rows with [.sample()]
print(df_apps.sample(5))

# Remove the columns called `Last_Updated` and `Android_Version` from the DataFrame. We will not use these columns.
print(df_apps.drop(columns=['Last_Updated', 'Android_Ver'],axis=1, inplace=True))
print(df_apps.head())

# How may rows have a NaN value (not-a-number) in the Ratings column?
print(df_apps.Rating.isna().values.any())
# True

# Create DataFrame called `df_apps_clean` that does not include these rows.
df_apps_clean = df_apps.dropna()
print(df_apps_clean.shape)
# (9367, 10)

# Are there any duplicates in data? Check for duplicates using the [.duplicated()] function.
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape) # (476, 10)
print(duplicated_rows.head())

# How many entries can you find for the "Instagram" app?
print(df_apps_clean.duplicated())
print(df_apps_clean[df_apps_clean['App']=='Instagram']) # Reviews are not the same
#              App Category  Rating   Reviews  Size_MBs       Installs  Type Price Content_Rating  Genres
# 10806  Instagram   SOCIAL    4.50  66577313      5.30  1,000,000,000  Free     0           Teen  Social
# 10808  Instagram   SOCIAL    4.50  66577446      5.30  1,000,000,000  Free     0           Teen  Social
# 10809  Instagram   SOCIAL    4.50  66577313      5.30  1,000,000,000  Free     0           Teen  Social
# 10810  Instagram   SOCIAL    4.50  66509917      5.30  1,000,000,000  Free     0           Teen  Social

# Use [.drop_duplicates()] to remove any duplicates from `df_apps_clean`.
df_apps_clean = df_apps_clean.drop_duplicates()
print(df_apps_clean[df_apps_clean['App']=='Instagram']) # only remove one entry (Reviews = 66577313)
#              App Category  Rating   Reviews  Size_MBs       Installs  Type Price Content_Rating  Genres
# 10806  Instagram   SOCIAL    4.50  66577313      5.30  1,000,000,000  Free     0           Teen  Social
# 10808  Instagram   SOCIAL    4.50  66577446      5.30  1,000,000,000  Free     0           Teen  Social
# 10810  Instagram   SOCIAL    4.50  66509917      5.30  1,000,000,000  Free     0           Teen  Social

print(df_apps_clean.shape)
# (8891, 10)

# Identify which apps are the highest rated.
print(df_apps_clean.sort_values("Rating", ascending=False).head())
# What problem might you encounter if you rely exclusively on ratings alone to determine the quality of an app?
# only show the entries that have few Reviews
#                       App            Category  Rating  Reviews  Size_MBs Installs  Type  Price Content_Rating            Genres
# 21    KBA-EZ Health Guide             MEDICAL    5.00        4     25.00        1  Free      0       Everyone           Medical
# 1573       FHR 5-Tier 2.0             MEDICAL    5.00        2      1.20      500  Paid  $2.99       Everyone           Medical
# 1096             BG Guide    TRAVEL_AND_LOCAL    5.00        3      2.40      100  Free      0       Everyone    Travel & Local
# 1095         Morse Player              FAMILY    5.00       12      2.40      100  Paid  $1.99       Everyone         Education
# 1092                DG TV  NEWS_AND_MAGAZINES    5.00        3      5.70      100  Free      0       Everyone  News & Magazines

# What's the size in megabytes (MB) of the largest Android apps in the Google Play Store.
print(df_apps_clean.sort_values("Size_MBs", ascending=False).head())
#                                   App   Category  Rating  Reviews  Size_MBs     Installs  Type Price Content_Rating                  Genres
# 7926                        Post Bank    FINANCE    4.50    60449    100.00    1,000,000  Free     0       Everyone                 Finance
# 9944     Gangster Town: Vice District     FAMILY    4.30    65146    100.00   10,000,000  Free     0     Mature 17+              Simulation
# 9942   Talking Babsy Baby: Baby Games  LIFESTYLE    4.00   140995    100.00   10,000,000  Free     0       Everyone  Lifestyle;Pretend Play
# 9945                  Ultimate Tennis     SPORTS    4.30   183004    100.00   10,000,000  Free     0       Everyone                  Sports
# 10687          Hungry Shark Evolution       GAME    4.50  6074334    100.00  100,000,000  Free     0           Teen                  Arcade

# Based on the data, do you think there could be limit in place or can developers make apps as large as they please?
# Yes, the limit is 100M

# Which apps have the highest number of reviews?
print(df_apps_clean.sort_values("Reviews", ascending=False).head(50)) # type: Free
#                       App       Category  Rating   Reviews  Size_MBs       Installs  Type Price Content_Rating         Genres
# 10805            Facebook         SOCIAL    4.10  78158306      5.30  1,000,000,000  Free     0           Teen         Social
# 10811            Facebook         SOCIAL    4.10  78128208      5.30  1,000,000,000  Free     0           Teen         Social
# 10785  WhatsApp Messenger  COMMUNICATION    4.40  69119316      3.50  1,000,000,000  Free     0       Everyone  Communication
# 10797  WhatsApp Messenger  COMMUNICATION    4.40  69109672      3.50  1,000,000,000  Free     0       Everyone  Communication
# 10808           Instagram         SOCIAL    4.50  66577446      5.30  1,000,000,000  Free     0           Teen         Social

# Are there any paid apps among the top 50?
# No, there are all free.

# Plotly Pie and Donut Charts - Visualise Categorical Data: Content Ratings
ratings = df_apps_clean.Content_Rating.value_counts()
print(ratings)
# Everyone           7094
# Teen               1022
# Mature 17+          411
# Everyone 10+        360
# Adults only 18+       3
# Unrated               1
# Name: Content_Rating, dtype: int64

import plotly.express as px
import plotly.io as pio

fig0 = px.pie(labels=ratings.index, values=ratings.values)
# pio.show(fig0, renderer="browser")

fig1 = px.pie(
    labels=ratings.index,
    values=ratings.values,
    title="Content Rating",
    names=ratings.index,
)
fig1.update_traces(textposition='outside', textinfo='percent+label')
# pio.show(fig1, renderer="browser")

fig2 = px.pie(
    labels=ratings.index,
    values=ratings.values,
    title="Content Rating",
    names=ratings.index,
    hole=0.6,
)
fig2.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
# pio.show(fig2, renderer="browser")


# How many apps had over 1 billion (that's right - BILLION) installations?
print(df_apps_clean.sort_values("Installs", ascending=False).head())
#                                App       Category  Rating   Reviews  Size_MBs     Installs  Type Price Content_Rating         Genres
# 10729  LINE: Free Calls & Messages  COMMUNICATION    4.20  10790092      3.50  500,000,000  Free     0       Everyone  Communication
# 10752                  Cloud Print   PRODUCTIVITY    4.10    282460      4.00  500,000,000  Free     0       Everyone   Productivity
# 10735                     Snapchat         SOCIAL    4.00  17014787      5.30  500,000,000  Free     0           Teen         Social
# 10736                     Snapchat         SOCIAL    4.00  17014705      5.30  500,000,000  Free     0           Teen         Social
# 10737                     Snapchat         SOCIAL    4.00  17015352      5.30  500,000,000  Free     0           Teen         Social
# df_apps_clean[df_apps_clean['Installs']>=100_000_000] # not work, <class 'int'>
print(df_apps_clean)
#                                                    App Category  Rating   Reviews  Size_MBs       Installs  Type  Price Content_Rating   Genres
# 21                                 KBA-EZ Health Guide  MEDICAL    5.00         4     25.00              1  Free      0       Everyone  Medical
# 28                                            Ra Ga Ba     GAME    5.00         2     20.00              1  Paid  $1.49       Everyone   Arcade
# 47                                             Mu.F.O.     GAME    5.00         2     16.00              1  Paid  $0.99       Everyone   Arcade
# 82                                    Brick Breaker BR     GAME    5.00         7     19.00              5  Free      0       Everyone   Arcade
# 99     Anatomy & Physiology Vocabulary Exam Review App  MEDICAL    5.00         1      4.60              5  Free      0       Everyone  Medical
# ...                                                ...      ...     ...       ...       ...            ...   ...    ...            ...      ...
# 10835                                   Subway Surfers     GAME    4.50  27722264     76.00  1,000,000,000  Free      0   Everyone 10+   Arcade
# 10836                                   Subway Surfers     GAME    4.50  27723193     76.00  1,000,000,000  Free      0   Everyone 10+   Arcade
# 10837                                   Subway Surfers     GAME    4.50  27724094     76.00  1,000,000,000  Free      0   Everyone 10+   Arcade
# 10838                                   Subway Surfers     GAME    4.50  27725352     76.00  1,000,000,000  Free      0   Everyone 10+   Arcade
# 10840                                   Subway Surfers     GAME    4.50  27711703     76.00  1,000,000,000  Free      0   Everyone 10+   Arcade
print(df_apps_clean['Installs'].describe())
# count          8197
# unique           19
# top       1,000,000
# freq           1417
# Name: Installs, dtype: object

# How many apps just had a single install?
print(df_apps_clean[['App', 'Installs']].groupby('Installs').count())
#                 App
# Installs
# 1                 3
# 1,000           699
# 1,000,000      1486
# 1,000,000,000    49
# 10               69
# 10,000          989
# 10,000,000     1130
# 100             303
# 100,000        1110
# 100,000,000     369
# 5                 9
# 5,000           426
# 5,000,000       683
# 50               56
# 50,000          462
# 50,000,000      272
# 500             199
# 500,000         516
# 500,000,000      61

# Check the datatype of the Installs column.
print(df_apps_clean.info())
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 8891 entries, 21 to 10840
# Data columns (total 10 columns):
#  #   Column          Non-Null Count  Dtype
# ---  ------          --------------  -----
#  0   App             8891 non-null   object
#  1   Category        8891 non-null   object
#  2   Rating          8891 non-null   float64
#  3   Reviews         8891 non-null   int64
#  4   Size_MBs        8891 non-null   float64
#  5   Installs        8891 non-null   object
#  6   Type            8891 non-null   object
#  7   Price           8891 non-null   object
#  8   Content_Rating  8891 non-null   object
#  9   Genres          8891 non-null   object
# dtypes: float64(2), int64(1), object(7)
# memory usage: 764.1+ KB
# None

# Count the number of apps at each level of installations.
# Convert the number of installations (the Installs column) to a numeric data type.
# Hint: this is a 2-step process. You'll have make sure you remove non-numeric characters first.
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
print(df_apps_clean[['App', 'Installs']].groupby('Installs').count())
#              App
# Installs
# 1              3
# 5              9
# 10            69
# 50            56
# 100          303
# 500          199
# 1000         699
# 5000         426
# 10000        989
# 50000        462
# 100000      1110
# 500000       516
# 1000000     1486
# 5000000      683
# 10000000    1130
# 50000000     272
# 100000000    369
# 500000000     61
# 1000000000    49
print(df_apps_clean.sort_values("Installs", ascending=False).head(5))
#                       App       Category  Rating   Reviews  Size_MBs    Installs  Type Price Content_Rating         Genres
# 10840      Subway Surfers           GAME    4.50  27711703     76.00  1000000000  Free     0   Everyone 10+         Arcade
# 10797  WhatsApp Messenger  COMMUNICATION    4.40  69109672      3.50  1000000000  Free     0       Everyone  Communication
# 10811            Facebook         SOCIAL    4.10  78128208      5.30  1000000000  Free     0           Teen         Social
# 10810           Instagram         SOCIAL    4.50  66509917      5.30  1000000000  Free     0           Teen         Social
# 10808           Instagram         SOCIAL    4.50  66577446      5.30  1000000000  Free     0           Teen         Social

# How many apps had over 1 billion (that's right - BILLION) installations?
print(len(df_apps_clean[df_apps_clean['Installs']>=1000_000_000]))
# 49

# Convert the price column to numeric data.
# Then investigate the top 20 most expensive apps in the dataset.
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace(',', "").str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
print(df_apps_clean[['App', 'Price']].groupby('Price').count())
#          App
# Price
# 0.00    8278
# 0.99     105
# 1.00       2
# 1.20       1
# 1.29       1
# ...      ...
# 299.99     1
# 379.99     1
# 389.99     1
# 399.99    11
# 400.00     1
# [73 rows x 1 columns]

# Remove all apps that cost more than $250 from the `df_apps_clean` DataFrame.
print(df_apps_clean.sort_values("Price", ascending=False).head(20))
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
print(df_apps_clean.sort_values('Price', ascending=False).head(5))
#                             App   Category  Rating  Reviews  Size_MBs  Installs  Type  Price Content_Rating     Genres
# 2281  Vargo Anesthesia Mega App    MEDICAL    4.60       92     32.00      1000  Paid  79.99       Everyone    Medical
# 1407               LTC AS Legal    MEDICAL    4.00        6      1.30       100  Paid  39.99       Everyone    Medical
# 2629           I am Rich Person  LIFESTYLE    4.20      134      1.80      1000  Paid  37.99       Everyone  Lifestyle
# 2481    A Manual of Acupuncture    MEDICAL    3.50      214     68.00      1000  Paid  33.99       Everyone    Medical
# 4264    Golfshot Plus: Golf GPS     SPORTS    4.10     3387     25.00     50000  Paid  29.99       Everyone     Sports

# Add a column called 'Revenue_Estimate' to the DataFrame.
# This column should hold the price of the app times the number of installs.
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)

# What are the top 10 highest grossing paid apps according to this estimate?
# Out of the top 10 highest grossing paid apps, how many are games?
print(df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10])
#                                 App       Category  Rating  Reviews  Size_MBs  Installs  Type  Price Content_Rating                     Genres  Revenue_Estimate
# 9224                      Minecraft         FAMILY    4.50  2375336     19.00  10000000  Paid   6.99   Everyone 10+  Arcade;Action & Adventure     69,900,000.00
# 9220                      Minecraft         FAMILY    4.50  2376564     19.00  10000000  Paid   6.99   Everyone 10+  Arcade;Action & Adventure     69,900,000.00
# 8825                  Hitman Sniper           GAME    4.60   408292     29.00  10000000  Paid   0.99     Mature 17+                     Action      9,900,000.00
# 7151  Grand Theft Auto: San Andreas           GAME    4.40   348962     26.00   1000000  Paid   6.99     Mature 17+                     Action      6,990,000.00
# 7477            Facetune - For Free    PHOTOGRAPHY    4.40    49553     48.00   1000000  Paid   5.99       Everyone                Photography      5,990,000.00
# 7977        Sleep as Android Unlock      LIFESTYLE    4.50    23966      0.85   1000000  Paid   5.99       Everyone                  Lifestyle      5,990,000.00
# 6594            DraStic DS Emulator           GAME    4.60    87766     12.00   1000000  Paid   4.99       Everyone                     Action      4,990,000.00
# 6082                   Weather Live        WEATHER    4.50    76593      4.75    500000  Paid   5.99       Everyone                    Weather      2,995,000.00
# 6856                        Threema  COMMUNICATION    4.50    51110      3.50   1000000  Paid   2.99       Everyone              Communication      2,990,000.00
# 7044                         Tasker          TOOLS    4.60    43045      3.40   1000000  Paid   2.99       Everyone                      Tools      2,990,000.00

# Plotly Bar Charts & Scatter Plots: Analysing App Categories
print(df_apps_clean.Category.nunique())
# 33
top10_category = df_apps_clean.Category.value_counts()[:10]
print(top10_category)
# FAMILY             1714
# GAME               1074
# TOOLS               733
# PRODUCTIVITY        334
# FINANCE             311
# PERSONALIZATION     310
# COMMUNICATION       307
# PHOTOGRAPHY         304
# MEDICAL             302
# LIFESTYLE           301
# Name: Category, dtype: int64
# None
bar = px.bar(
    x = top10_category.index, # index = category name
    y = top10_category.values
)
# bar.show()

import matplotlib.pyplot as plt
# plt.figure()
bar = px.bar(
    x = top10_category.index, # index = category name
    y = top10_category.values
)
# plt.imshow(bar)
# plt.show()

category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)
print(category_installs.head())
#                    Installs
# Category
# EVENTS             15949410
# BEAUTY             26916200
# PARENTING          31116110
# MEDICAL            42162676
# AUTO_AND_VEHICLES  53129800

h_bar = px.bar(
    x = category_installs.Installs,
    y = category_installs.index,
    orientation='h'
)
h_bar.show()

h_bar = px.bar(
    x = category_installs.Installs,
    y = category_installs.index,
    orientation='h',
    title='Category Popularity'
)
h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()

# First, create a DataFrame that has the number of apps in one column and the number of installs in another
cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
print(cat_number)
#                       App
# Category
# ART_AND_DESIGN         62
# AUTO_AND_VEHICLES      73
# BEAUTY                 42
# BOOKS_AND_REFERENCE   177
# BUSINESS              270
# COMICS                 58
# COMMUNICATION         307
# DATING                159
# EDUCATION             129
# ENTERTAINMENT         111
# EVENTS                 45
# FAMILY               1714
# FINANCE               311
# FOOD_AND_DRINK        106
# GAME                 1074
# HEALTH_AND_FITNESS    262
# HOUSE_AND_HOME         68
# LIBRARIES_AND_DEMO     65
# LIFESTYLE             301
# MAPS_AND_NAVIGATION   124
# MEDICAL               302
# NEWS_AND_MAGAZINES    214
# PARENTING              50
# PERSONALIZATION       310
# PHOTOGRAPHY           304
# PRODUCTIVITY          334
# SHOPPING              201
# SOCIAL                244
# SPORTS                286
# TOOLS                 733
# TRAVEL_AND_LOCAL      205
# VIDEO_PLAYERS         160
# WEATHER                75
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
print(cat_merged_df.sort_values('Installs', ascending=False).head())
# The dimensions of the DataFrame are: (33, 2)
#                 App     Installs
# Category
# GAME           1074  31543862717
# COMMUNICATION   307  24152241530
# SOCIAL          244  12513841475
# PRODUCTIVITY    334  12463070180
# TOOLS           733  11440724500

# Then use the [plotly express examples from the documentation] to create scatter plot that looks like this.
fig = px.scatter(x=cat_merged_df.App, y=cat_merged_df.Installs)
# fig.show()

fig = px.scatter(
    cat_merged_df,
    x=cat_merged_df.App,
    y=cat_merged_df.Installs,
    title='Category Concentration',
    size='App',
    hover_name=cat_merged_df.index,
    color='Installs'
)
fig.update_layout(xaxis_title='Number of Apps(Lower=More Concentrated)', yaxis_title='Installs')
fig.update_layout(yaxis=dict(type='log'))
fig.show()

# How many different types of genres are there?
# Can an app belong to more than one genre?
print(df_apps_clean.Genres.nunique())
# 115
# Check what happens when you use .value_counts() on a column with nested values?
print(df_apps_clean.Genres.value_counts().sort_values(ascending=True)[:5])
# Lifestyle;Pretend Play                 1
# Strategy;Creativity                    1
# Parenting;Brain Games                  1
# Health & Fitness;Action & Adventure    1
# Arcade;Pretend Play                    1
# Name: Genres, dtype: int64

print(df_apps_clean.stack())
# 21     App                 KBA-EZ Health Guide
#        Category                        MEDICAL
#        Rating                             5.00
#        Reviews                               4
#        Size_MBs                          25.00
#                                   ...
# 10840  Type                               Free
#        Price                              0.00
#        Content_Rating             Everyone 10+
#        Genres                           Arcade
#        Revenue_Estimate                   0.00
# Length: 97636, dtype: object


# See if you can work around this problem by using the .split() function and the DataFrame's [.stack() method].
# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
# We now have a single column with shape: (9323,)
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')
# Number of genres: 53
print(num_genres)
# Tools                      733
# Education                  626
# Entertainment              534
# Action                     364
# Productivity               334
# Finance                    311
# Personalization            310
# Communication              308
# Photography                304
# Sports                     303
# Lifestyle                  302
# Medical                    302
# Business                   270
# Health & Fitness           264
# Casual                     255
# Social                     244
# Arcade                     220
# News & Magazines           214
# Simulation                 210
# Travel & Local             205
# Shopping                   201
# Books & Reference          179
# Video Players & Editors    163
# Dating                     159
# Puzzle                     143
# Action & Adventure         125
# Maps & Navigation          124
# Role Playing               116
# Racing                     114
# Food & Drink               106
# Strategy                   105
# Educational                 97
# Adventure                   89
# Pretend Play                79
# Weather                     75
# Auto & Vehicles             73
# House & Home                68
# Brain Games                 68
# Art & Design                65
# Libraries & Demo            65
# Board                       60
# Comics                      58
# Parenting                   50
# Card                        48
# Events                      45
# Beauty                      42
# Music & Video               41
# Casino                      37
# Creativity                  36
# Trivia                      28
# Word                        27
# Music                       23
# Music & Audio                1
# dtype: int64

# Can you create this chart with the Series containing the genre data?
bar = px.bar(
    x = num_genres.index[:15],
    y = num_genres.values[:15],
    color = num_genres.values[:15],
    title='Top Genres',
    color_continuous_scale='Agsunset',
)
bar.update_layout(
    xaxis_title='Genre',
    yaxis_title='Number of Apps',
    coloraxis_showscale=False
)
bar.show()

# Grouped Bar Charts: Free vs. Paid Apps per Category
print(df_apps_clean.Type.value_counts())
# Free    8278
# Paid     598
# Name: Type, dtype: int64
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
print(df_free_vs_paid.head())
#             Category  Type  App
# 0     ART_AND_DESIGN  Free   59
# 1     ART_AND_DESIGN  Paid    3
# 2  AUTO_AND_VEHICLES  Free   72
# 3  AUTO_AND_VEHICLES  Paid    1
# 4             BEAUTY  Free   42

print(df_free_vs_paid[df_free_vs_paid.Type=="Free"].head())
#               Category  Type  App
# 0       ART_AND_DESIGN  Free   59
# 2    AUTO_AND_VEHICLES  Free   72
# 4               BEAUTY  Free   42
# 5  BOOKS_AND_REFERENCE  Free  169
# 7             BUSINESS  Free  261

# Use the plotly express bar [chart examples] and the [.bar() API reference] to create this bar chart:
import plotly.graph_objects as go

g_bar = px.bar(
    df_free_vs_paid,
    x='Category',
    y='App',
    title='Free vs Paid Apps by Category',
    color='Type',
    barmode='group'
)
g_bar.update_layout(
    xaxis_title='Category',
    yaxis_title='Number of Apps',
    xaxis={'categoryorder':'total descending'},
    yaxis=dict(type='log')
)
g_bar.show()

# Create a box plot that shows the number of Installs for free versus paid apps.
# How does the median number of installations compare? Is the difference large or small?
box = px.box(
    df_apps_clean,
    y='Installs',
    x='Type',
    color='Type',
    notched=True,
    points='all',
    title='How Many Downloads are Paid Apps Giving Up?'
)
box.update_layout(yaxis=dict(type='log'))
box.show()

# Plotly Box Plots: Revenue by App Category
df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']

box = px.box(
    df_paid_apps,
    y='Revenue_Estimate',
    x='Category',
    title='How Much Can Paid Apps Earn?')
box.update_layout(
    xaxis={'categoryorder':'min ascending'},
    yaxis=dict(type='log')
)
box.show()

# How Much Can You Charge? Examine Paid App Pricing Strategies by Category
# What is the median price price for a paid app?
print(df_paid_apps.Price.median())
# 2.99
df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']

box = px.box(
    df_paid_apps,
    y='Price',
    x='Category',
    title='Price per Category'
)
box.update_layout(
    xaxis={'categoryorder':'max descending'},
    yaxis=dict(type='log')
)
box.show()