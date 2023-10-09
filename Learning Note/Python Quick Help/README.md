# Markdown
```
1. # for bold title
2. double space for new line
3. **text** for bold  
```

# Helpful Syntax
```
df = pd.read_excel(https://raw.githubusercontent.com/HaomingChen1998/excel.xlsx) # Read csv from github: change github.com to raw.githubusercontent.com
pd.options.display.max_columns = 200
plt.style.use('ggplot')
df.drop(['column_name'], axis=1)
df.rename(columns={'old_name':'new_name', 'old_name2':'new_name2'})
df.columns = df.columns.str.replace(' ', '_')          # Replace space with underscore.
df.name.str.split(' ', expand=True)     # Split the names under the name column into different columns when there is a space.
df.groupby('from_user').size().to_frame('total_emails').reset_index() # Group by from users, and count how many times the same value repeated.  to_frame gives this count column a name. reset_index treats index as column, in this case, it shows from_user column.
df.column_name.shift(1) # Shift that column down by 1
df['rank'] = df.total_emails.rank(method='first', ascending=False) # method='first' is like row_number, dense is like dense_rank
df['Timestamp'] = df['Timestamp'].astype('datetime64[ns]')
df.query('Coaster_Name == "Beach"')           # show data when coaster_name = beach
df.query('pricecategory.isin(["Low", "High"])')
dma13.query('dma.str.contains("atlanta", case=False)') # Similar to SQL ilike, case=False: case-insensitive, you can do without.
df['Gender'].value_counts()                     # count the number of occurrences of each unique value. Ex: Male 30, Female 29
pd.DataFrame(np.random.rand(4,8))                # Create an example DataFrame to quickly show something
pd.to_numeric(df.col_three, errors='coerce'.fillna(0)
movies[movies.genre.isin(['Action', 'Drama', 'Western'])] # Show rows where genre column is Action OR Drama OR Western. Add~ before movies.genre for is not.
pd.cut(titanic.Age, bins=[0, 18, 25, 99], labels=['child', 'young adult', 'adult']) Convert continuous data into categorical data, age 0-18 for child, 18-25 for young adult, etc.
df.columns = df.columns.str.replace(' ', '_').str.lower()
iloc[] only accept numbers inside [], but when you refer to a column name inside [], you should use loc. Ex:df1.loc[:3, 'column_name'].

```

# Python Environment VScode Syntax

```
- pip freeze > requirements.txt
- pip install -r requirements.txt # Installs all the packages from requirement.txt
```

# Visualization with Pandas
There are several plot types built into pandas; most of them are statistical by nature:  

```
df.plot.hist()
df.plot.barh()
df.plot.line()
df.plot.area()
df.plot.hexbin()
df.plot.bar()
df.plot.scatter()
df.plot.box()
df.plot.kde()
df.plot.pie()
```

You can also call specific plots by passing their name as an argument, as with 
df.plot (kind=' area').

EXAMPLES:  
```
df['Column_Name'].plot.hist()
```   
If you can see the edge, you can modify the code like hist(edgecolor='k')   
If you want more bars, hist(bin=20), the number can be whatever number of bars.  

```
title='title_name'
df.set_xlabel('xlabel_name')
df.set_ylabel('ylabel_name')
bins=20
```

# Visualization with Seaborn

```
sns.scatterplot(x='column_name', y='column_name', hue='Year', data=df)
sns.pairplot(df, var=['column_name', 'column_name2'], hue='column_name')

df_corr = df[['column_name', 'column_name2']].dropna().corr()
sns.heatmap(df_corr, annot=True)

plt.show()
```
