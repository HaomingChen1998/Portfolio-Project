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

# Different ways to export as csv from vscode
results.to_csv(r'C:\Users\Cody\Desktop\results.csv', index=False)

results.to_csv('C:/Users/Cody/Desktop/results.csv', index=False)

results.to_csv('results.csv', index=False)


import csv
# exporting a string variable into the csv file
input_variable = "GeeksForGeeks"
# Example.csv gets created in the current working directory
with open('Example.csv', 'w', newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerow(input_variable)


# Create a dataframe with just rows (no column names)
# Specify each row as a list
data = [
    ['atlanta', 'chicago', 'las vegas'],
    ['austin', 'oakland', 'oklahoma city'],
    ['baltimore', 'philadelphia', 'reno'],
    ['baton rouge', 'cincinnati', 'portland'],
    ['boston', 'jacksonville', 'new orleans']
]
data = pd.DataFrame(data) # Create DataFrame using the list of lists
It will look like below:
             0             1              2
0      atlanta       chicago      las vegas
1       austin       oakland  oklahoma city
2    baltimore  philadelphia           reno
3  baton rouge    cincinnati       portland
4       boston  jacksonville    new orleans


# Convert each row into a set
data_set = pd.DataFrame(data).apply(lambda x: pd.Series(x), axis=1)

# If include_markets_set is not a subset of any set in BestMarkets_aux_set, then error.
if not any(BestMarkets_aux_set.apply(lambda x: include_markets_set1.issubset(x))):
    message = (
        f"Error: The following market combination from your 'include_markets' is not available:\n\n"
        f"{include_markets_set1}\n\n"
        "Available combinations are:\n"
        f"{BestMarkets_aux_set}."
    )
    logger.error(message)
    raise ValueError(message)

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


# VSCode Shorcut:
```
# Comment out multiple lines with #
Ctrl L, Ctrl /
```

# Git: Share my folder to collaborate with others:
1. Login to my github on browser
2. Click on my profile -> Your repositories -> New
3. Setting -> Collaborators -> Add People # Invite people to my repo
4. Open terminal to run the following code:
```
# Change directory to the folder that I want to share
cd [Folder_Path]

# Turn current folder into a git repo (a folder that git can track)
git init

# rename current branch to main
git branch -M main

# Ex: username = haomingchen1998, repo_name = AutoHotkey.git
git remote add origin https://github.com/[username]/[repo_name].git

# verify if the above remote url is added locally.
git remote -v

# Input your info
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# Add all the files from that folder locally to GitHub.
git add .

# Confirm your changes
git commit -m "your_message_here"

# if error, refer back to "git remote -v" code line
git push -u origin main
```
How others can collaborate me:
1. Go to github -> next to profile icon, click on inbox icon.
2. Accept the invite.
3. Then I can download as zip -> unzip -> open that folder using VSCode. Alternatively you can clone.

# Python Virtual Environment VSCode Syntax

```
# Create a new folder in desktop for storing your virtual environment later

# Select a folder location (the folder you created above) to store your virtual environment from VSCODE: File -> Folder

# Make sure you have already installed your desire python version which can be downloaded at https://www.python.org/downloads/

# Create a virtual environment using the path of your desired python version, replace the python path accordingly.
C:\Users\codchen1\AppData\Local\Programs\Python\Python312\python.exe -m venv .

# Allow Activate.ps1 to run (executed from the VSCode terminal)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Activate this environment using "& [path to Activate.ps1 file from your virtual environment folder]"
& c:/Users/Cody/Desktop/Default_Python/Scripts/Activate.ps1

# Check virtual environment being used right now, the top python path has priority.
where.exe python

# Install all the packages from requirements.txt
pip install -r requirements.txt

# Uninstall all the packages from requirements.txt
pip uninstall -r requirements.txt -y

# Store all the pip packages in requirements.txt
pip freeze > requirements.txt

# Check what packages are installed
pip list

# Check if a specific package is installed
pip show [package_name]

# If pip install didn't install in your virtual environment folder, use the full path to the Python interpreter in your virtual environment to install.
# requirements.txt file should be located at the main folder.
C:\Users\Cody\Desktop\Default_Python\Default_Python\Scripts\python.exe -m pip install -r requirements.txt

# Genereate requirements.txt file with only a few selected packages. You need to import the packages you want to include first.
pip install pipreqs --force
pip freeze > requirements.txt # Generate requirements.txt file that includes all packages installed.

# Revert to a Previous Git Version (revert locally only)
git checkout -f HEAD~1

# Revert to a Previous Git Version (revert locally, then push out as a new commit [no commits are deleted])
git revert HEAD~1
git push origin main

# Reset to a Previous Git Version (Local files will be deleted forcefully, commits after the reverted commit will be deleted)
git reset --hard HEAD~3 # Revert back to 3rd commits locally
git push -f origin main # Force push that local update to GitHub


# Get rid of all Outgoing/Incoming changes
git reset --hard origin/development 

# Push a single file
git commit -m 'your comment' path/to/your/file.txt
then push to the branch

# Creates a new branch and push to that branch
git branch newBranch master # Creates a new branch called "newBranch" base on the master branch.
git checkout newBranch # Switches to "newBranch" branch
git push -u origin newBranch # Pushes to that branch
```

**Error Handling for Using Virtual Environment:**
```
# Fatal error in launcher: Unable to create process
python -m pip install --upgrade --force-reinstall pip # Fatal error in launcher: Unable to create process

# If unable to push:
1. commit
2. then push
3. If not successful, then pull.
4. Maybe conflict, If so, click on each file with conflict symbol, and then click on Conflict Merge Panel. Check the view's name to see if the one on the left or right is mine. Click on accept or ignore.
5. Then push again.
6. git push --force  ; You can also try force push

# If unable to discard all my changes
1. Need to save all first.
2. Menu button next to the source control
3. Changes -> Discard all changes

OR
1. Stash the file that I wanna keep. (from the menu button next to the source control. Save in a safe place, and we gonna bring it back later)
2. Discard the change for the remaining unwanted files
3. Pop stash (bring back the file that I saved before back)


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


# Python Github Package Installation

```
# git+the link you get from the github main page -> green "Code" button -> copy the https link.
pip install "git+https://github.com/google/matched_markets.git"

# Download the setup.py file and place it to the environment folder.
python setup.py install

# If you downloaded package that has "setup.py" in root folder, you can install it by running
python setup.py install
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


# Run Python Code from CMD

```
# Activate Virtual Environment
cd C:\Users\codchen1\Desktop\Main.Py\Scripts\
call activate.bat

# Activate Virtual Environment (Method 2)
"C:\Users\codchen1\Desktop\Main.Py\Scripts\activate.bat"

# Run a python file using a specific virtual environment (Make sure activate the environment first)
"C:\Users\codchen1\Desktop\Default_Python\Scripts\python.exe" -u "C:\Users\codchen1\Desktop\Main.Py\date_cal.py"

pause # See the output before terminal closes
& runs the second command on the line whether the first command comes back successfully or not.
&& runs the second command on the line when the first command comes back successfully (i.e. errorlevel == 0).
|| runs the second command when the first command is unsuccessful (i.e. errorlevel != 0).
```

# Prevent Computer from Going to Sleep  
It detects mouse movement every 5 seconds, if no movement is detected within 5 seconds, then it will press Num Key. If movement is detected within 5 seconds, then no action will be performed.
```
1. Download stay_awake folder.
2. Install all the required packages from requirements.txt with below code in powershell / VSCode terminal:
pip install -r requirements.txt
3. Then run the code inside stay_awake.py file.

----------------------------------------[Optional Steps to automate it further]------------------------------------------------------------------------------------------------------
Launching the script on system startup is also possible if you follow below steps:

1. Place the stay_awake.bat file in the virtual environment main folder
(it will loops through all files inside this main folder to look for activate.bat and stay_awake.py file paths)

2. Make sure both the activate.bat and stay_awake.py files are both placed within this virtual folder
(these two files can be placed anywhere in this folder)

3. Create a shortcut of this stay_awake.bat file, then place it inside the windows startup folder by doing Win+R then type shell:startup
```

# Building Local GPT4 for free using Python
```
; Run the following code in Python
pip install g4f -U
g4f gui -port 8080
; Run the following code in browser
http://127.0.0.1:8080/chat/
; Run in cmd if you don't want to run in Python:
"C:\Virtual_Environment_3.11\Scripts\python.exe" -c "import g4f; g4f.gui('-port', '8080')"
```




