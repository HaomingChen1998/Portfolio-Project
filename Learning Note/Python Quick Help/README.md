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
# Select location to store your virtual environment: File -> Folder
C:\Users\codchen1\AppData\Local\Programs\Python\Python312\python.exe -m venv geolift # path to the python version you want to use, make sure this python version is downloaded first from https://www.python.org/downloads/. Geolift is the name of that virtual environment you are about to create.
# Run the activate.bat file to activate.
pip install -r requirements.txt # Installs all the packages from requirements.txt
pip install pipreqs --force# Genereate requirements.txt file with only a few selected packages. You need to import the packages you want to include first.
pip freeze > requirements.txt # Generate requirements.txt file that includes all packages installed.
# If you downloaded package that has "setup.py" in root folder, you can install it by running
python setup.py install
```

```
# Check Python and package version
import pandas as pd
import numpy as np
import sys
# Python 3.12.0
# NumPy 1.26.0
# Pandas 2.1.1

print(f'pandas version: {pd.__version__}')
print(f'numpy version: {np.__version__}')
print(f'Python version: {sys.version}')
```

```
# Troubleshoot:
python -m pip install --upgrade --force-reinstall pip # Fatal error in launcher: Unable to create process
```

# Python Github Package Installation

```
pip install "git+https://github.com/google/matched_markets.git" # git+the link you get from the github main page -> green "Code" button -> copy the https link.
python setup.py install # Download the setup.py file and place it to the environment folder.
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
