import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')

# Session 555
# Used the .head() method to peek at the top 5 rows of our dataframe
df.head()
print(f"head = {df.head()}")

# To see the number of rows and columns we can use the shape attribute
df.shape
print(f"shape = {df.shape}")

# We can access the column names directly with the columns attribute.
df.columns
print(f"columns = {df.columns}")

# To look for NaN (Not A Number) values in our dataframe.
df.isna()
print(f"isna = {df.isna()}")

# Check the last couple of rows in the dataframe
df.tail()
print(f"tail = {df.tail()}")

# use the .dropna() method to delete the Last Row
clean_df = df.dropna()
clean_df.tail()
print(f"clean_df = {clean_df.tail()}")

# Session 556
# To access a particular column from a data frame
clean_df['Starting Median Salary']
print(f"clean_df_sal = {clean_df['Starting Median Salary']}")

# To find the highest starting salary we can simply chain the .max() method.
clean_df['Starting Median Salary'].max()
print(f"clean_df_sal_max = {clean_df['Starting Median Salary'].max()}")

# To know the row number or index
clean_df['Starting Median Salary'].idxmax()
print(f"clean_df_sal_idmax = {clean_df['Starting Median Salary'].idxmax()}") # 43

# To see the name of the major that corresponds to that particular row, we can use the .loc (location) property.
clean_df['Undergraduate Major'].loc[43]
print(f"clean_df_major_43 = {clean_df['Undergraduate Major'].loc[43]}") # Physician Assistant
# using the double square brackets notation to achieve exactly the same thing
clean_df['Undergraduate Major'][43]
print(f"clean_df_major_43 = {clean_df['Undergraduate Major'][43]}") # Physician Assistant

# Challenge
print("Challenge")
# What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
mid_sal_idmax = clean_df['Mid-Career Median Salary'].idxmax()
print(f"mid_sal_idmax = {mid_sal_idmax}") # 8
mid_sal_max_major = clean_df['Undergraduate Major'][mid_sal_idmax]
print(f"mid_sal_max_major = {mid_sal_max_major}") # Chemical Engineering

# Which college major has the lowest starting salary and how much do graduates earn after university?
start_sal_idmin = clean_df['Starting Median Salary'].idxmin()
start_sal_min_major = clean_df['Undergraduate Major'][start_sal_idmin]
print(f"start_sal_min_major = {start_sal_min_major}") # Spanish

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 
mid_sal_idmin = clean_df['Mid-Career Median Salary'].idxmin()
mid_sal_min_major = clean_df['Undergraduate Major'][mid_sal_idmin]
print(f"mid_sal_min_major = {mid_sal_min_major}") # Education

# Session 558
# Pandas allows us to do simple arithmetic with entire columns, so all we need to do is take the difference between the two columns:
clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# Alternatively, you can also use the .subtract() method.
clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
# The output of this computation will be another Pandas dataframe column. We can add this to our existing dataframe with the .insert() method:
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col) # 1 = insert position 1 = second column
clean_df.head()

# Sorting by the Lowest Spread
low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()
print(f"low_risk = {low_risk[['Undergraduate Major', 'Spread']].head()}")

# Challenge
# find the degrees with the highest potential? Find the top 5 degrees with the highest values in the 90th percentile. 
high_90th = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
high_90th[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()
print(f"high_90th = {high_90th[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()}")

# find the degrees with the greatest spread in salaries.
high_spread = clean_df.sort_values('Spread', ascending=False)
high_spread[['Undergraduate Major', 'Spread']].head()
print(f"high_spread = {high_spread[['Undergraduate Major', 'Spread']].head()}")

high_risk = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
high_risk[['Undergraduate Major', 'Mid-Career Median Salary']].head()
print(f"high_risk = {high_risk[['Undergraduate Major', 'Mid-Career Median Salary']].head()}")

# Session 560
clean_df.groupby('Group').count()
print(f"groupby_count = {clean_df.groupby('Group').count()}")
clean_df.groupby('Group').mean()
# print(f"groupby_mean = {clean_df.groupby('Group').mean()}")

pd.options.display.float_format = '{:,.2f}'.format 
