import pandas as pd
import matplotlib.pyplot as plt


# df = pd.read_csv('QueryResults.csv')
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# Look at the first and last 5 rows of the DataFrame.
df.head()
print(f"head = {df.head()}")

df.tail()
print(f"tail = {df.tail()}")
# How many rows and how many columns does it have?
df.shape
print(f"shape = {df.shape}")

# Count the number of entries in each column.
entry_counts = df.count()
print(entry_counts)


mask = df["TAG"]=="C#"
print(mask)

# Can you figure out how to count the number of posts per language?
df.groupby('TAG').sum()
print(f"groupby_TAG_sum = {df.groupby('TAG').sum()}")

# Which programming language had the most number of posts since the creation of Stack Overflow?
high_posts = df.sort_values('POSTS', ascending=False)
high_posts.head()
print(f"high_posts = {high_posts.head()}") # python*5

# Can you count how many months of posts exist for each programming language?
df.groupby('TAG').count()
print(f"groupby_TAG_count = {df.groupby('TAG').count()}")

# Session 566: Data Cleaning: Working with Time Stamps
df['DATE'][1]
print(f"df['DATE'][1] = {df['DATE'][1]}")
print(f"df.DATE[1]    = {df.DATE[1]}")

print(type(df['DATE'][1])) # <class 'str'>
# that is not very handy
# Pandas can help us convert the string to a timestamp using the to_datetime() method.
print(pd.to_datetime(df.DATE[1]))
print(type(pd.to_datetime(df.DATE[1]))) # <class 'pandas._libs.tslibs.timestamps.Timestamp'>

df.DATE = pd.to_datetime(df.DATE)
print(df.head())

# Session 567: Data Manipulation: Pivoting DataFrames
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
print(test_df)

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# pivoted_df = test_df.pivot_table(index='Age', columns='Actor', values='Power')
print(pivoted_df)

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
# reshaped_df = df.pivot_table(index='DATE', columns='TAG', values='POSTS', fill_value=0)
print(reshaped_df)

reshaped_df.shape
print(f"shape")
print(f"{reshaped_df.shape}")
reshaped_df.head()
print(f"head")
print(f"{reshaped_df.head()}")
reshaped_df.tail()
print(f"tail")
print(f"{reshaped_df.tail()}")
print(f"columns")
print(f"{reshaped_df.columns}")
print(f"sum")
print(f"{reshaped_df.sum()}")
print(f"count")
print(f"{reshaped_df.count()}") # some are not 145

# substitute the number 0 for each NaN value
reshaped_df.fillna(0, inplace=True) 
print(f"{reshaped_df.count()}") # all is 145
print(f"head")
print(f"{reshaped_df.head()}")
# check if there are any NaN values left in the entire DataFrame with this line
reshaped_df.isna().values.any()
print(f"{reshaped_df.isna().values.any()}") # False -> there are no any NaN values


# matplotlib
plt.figure(figsize=(8,5)) # need to be first
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.xlabel('Date', fontsize=7)
plt.ylabel('Number of Posts', fontsize=7)
plt.ylim(0, 35000)
# plt.plot(reshaped_df.index, reshaped_df['assembly'], label='assembly')
# plt.plot(reshaped_df.index, reshaped_df['c'], label='c')
# plt.plot(reshaped_df.index, reshaped_df['c#'], label='c#')
# plt.plot(reshaped_df.index, reshaped_df['python'], label='python')
# plot all lauguages
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], linewidth=2, label=reshaped_df[column].name)

print(plt.plot(reshaped_df.index, reshaped_df['assembly'])) # [<matplotlib.lines.Line2D object at 0x000001EB20C01A10>]
plt.legend(fontsize=7)
plt.show(block=False)

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=3).mean() # 越低越陡
roll_df = reshaped_df.rolling(window=6).mean() # 正常
roll_df = reshaped_df.rolling(window=12).mean() # 越高越平滑

plt.figure(figsize=(8,5))
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.xlabel('Date', fontsize=7)
plt.ylabel('Number of Posts', fontsize=7)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=8)
plt.show(block=False)

# Keep the plots open until manually closed
plt.show()