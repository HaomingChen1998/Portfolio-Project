![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Excel%201.png)
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Excel%202.png)
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Excel%203.png)
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Excel%204.png)
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Excel%205.png)
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Excel%206.png)

# Filter Data:
1. Ctrl+T
2. Insert Slicer
3. Choose what you want to filter by
4. Go to Slicer Tab on the top right corner.

# Freeze column (that is not the first column)
1. Click on a cell from the second column after the column you want to free
2. Click on "View" ribbon -> freeze panes -> freeze panes

# Percentile
1. =PERCENTILE.INC(), same as Percentile(), is more common that includes the first and last value. In other words, including kth percentile of 0 and 1.
2. =PERCENTILE.EXC() is less common that excludes the first and last value. In other words, excluding kth percentile of 0 and 1. Also, if you set k, aka "kth percentile" equals to 0, it will return NULL.
3. If there are empty cell in between, it’s going to treat it as if it doesn’t exist, and move the next number forward.

# Give name to the data under a column
1. Select all the data below a column (excluding column name itself)
2. Formula->Define Name
