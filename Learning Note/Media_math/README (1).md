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
result_name.to_csv(r'C:\Users\codchen1\Desktop\file_name.csv', index=False)

```

# Python Environment VScode Syntax

```
# Create a folder in desktop to store your virtual environment
# Select location to store your virtual environment from VSCODE: File -> Folder
# Make sure this python version is downloaded first from https://www.python.org/downloads/.
C:\Users\codchen1\AppData\Local\Programs\Python\Python312\python.exe -m venv . # Create a virtual environment
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # Allow Activate.ps1 to run
& c:/Users/Cody/Desktop/Default_Python/Scripts/Activate.ps1  # now activate this environment
where.exe python # check virtual environment being used right now, the top python path has priority.
.\pip.exe install -r ../requirements.txt
pip install -r requirements.txt # Installs all the packages from requirements.txt
# If pip install didn't install in virtual environment folder, use the full path to the Python interpreter in your virtual environment to install.
# requirements.txt file should be located at the main folder.
C:\Users\Cody\Desktop\Default_Python\Default_Python\Scripts\python.exe -m pip install -r requirements.txt
pip install pipreqs --force# Genereate requirements.txt file with only a few selected packages. You need to import the packages you want to include first.
pip freeze > requirements.txt # Generate requirements.txt file that includes all packages installed.
# If you downloaded package that has "setup.py" in root folder, you can install it by running
python setup.py install

if __name__ == "__main__"
When you import a function, it will run the function at the same time. The above function prevents this.
https://www.youtube.com/watch?v=o4XveLyI6YU

# ModuleNotFoundError  
add the following env entry to the launch.json configuration:
{
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": { "PYTHONPATH": "${workspaceRoot}"}
        }
    ]
}

# ModuleNoteFoundError solution 2
Create an __init__.py file in the same folder as the module you can't find.
Then type in   from .augsynth import *
The dot (.) before augsynth signifies a relative import. This means Python will look for the augsynth module in the same directory as the __init__.py file.
```
ModuleNoteFoundError solution 2  
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Module_Error.png)

```
# Check Python and package version
import pandas as pd
import numpy as np
import sys

# Pandas 2.1.1
# NumPy 1.26.0
# Python 3.12.0
print(f'pandas version: {pd.__version__}')
print(f'numpy version: {np.__version__}')
print(f'Python version: {sys.version}')
```

```
# Troubleshoot:
python -m pip install --upgrade --force-reinstall pip # Fatal error in launcher: Unable to create process

If unable to push:
1. commit
2. then push
3. If not successful, then pull.
4. Maybe conflict, If so, click on each file with conflict symbol, and then click on Conflict Merge Panel. Check the view's name to see if the one on the left or right is mine. Click on accept or ignore.
5. Then push again.

If unable to discard all my changes
1. Need to save all first.
2. Menu button next to the source control
3. Changes -> Discard all changes

OR
1. Stash the file that I wanna keep. (from the menu button next to the source control. Save in a safe place, and we gonna bring it back later)
2. Discard the change for the remaining unwanted files
3. Pop stash (bring back the file that I saved before back)
```

# Python Github Package Installation

```
pip install "git+https://github.com/google/matched_markets.git" # git+the link you get from the github main page -> green "Code" button -> copy the https link.
python setup.py install # Download the setup.py file and place it to the environment folder.
```

# Python Debug

```
Create a test.py file, and set it up like this:

# Import all the functions you have created from another file.
from geolift.auxiliary import fn_treatment, CorrelationCoefficient, limit_test_markets, MarketCorrelations

# Read dataset
data = pd.read_csv("tests/GeoDataReadProcessedData.csv")

# Set up testing:
def test_GeoLiftMarketSelection():
    #test this out having run_simulations return a dict with random generated numeric values
    returned_dict = GeoLiftMarketSelection(data = pd.read_csv("data/GeoDataReadProcessedData.csv"),
                                              treatment_periods = [10,15],
                                              N = [2,3,4,5],
                                              X = [],
                                              Y_id = "Y",
                                              location_id = "location",
                                              time_id = "time",
                                              effect_size = [0, 0.5, 0.05],
                                              lookback_window = 1,
                                              include_markets = ["chicago"],
                                              exclude_markets = ["honolulu"],
                                              holdout = [0.5, 1],
                                              cpic = 7.50,
                                              budget = 100000,
                                              alpha = 0.1,
                                              Correlations = True,
                                              fixed_effects = True,
                                              side_of_test = "two_sided")
    return returned_dict

if __name__=="__main__": # When a function gets imported, it would also be executed. This code prevents them from executing unless you run them manually.
    test_GeoLiftMarketSelection()
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

# Prevent Computer from Sleeping  
https://github.com/singhsidhukuldeep/stay-awake

```
pip install stay-awake
python -m stay-awake 5
```
Then put awake.bat file in the windows startup folder by doing Win+R, shell:startup

