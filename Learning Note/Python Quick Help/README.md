# Markdown
```
1. # for bold title
2. double space for new line
3. **text** for bold  
```

# Helpful Syntax
```
1. pd.set_option('max_columns', 200)
2. plt.style.use('ggplot')
3. df.drop(['column_name'], axis=1)
4. df.rename(columns={'old_name':'new_name', 'old_name2':'new_name2'})
5. df['Timestamp'] = df['Timestamp'].astype('datetime64[ns]')
6. df.query('Coaster_Name == "Beach"')           # show data when coaster_name = beach
7. df['Gender'].value_counts()                     # count the number of occurrences of each unique value. Ex: Male 30, Female 29
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

