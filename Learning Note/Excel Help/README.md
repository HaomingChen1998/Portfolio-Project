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

# Absolute vs Relative Reference [F4 Key]
1. Absolute Reference: when you drag down the formula, it locks on to a specific value, instead of looking for the value in next row to do the calculation.
2. Relative Reference: when you drag down the formula, it looks for the value in next row to do the calculation.

# Record Macro
1. View -> Macros -> Record Macro [Make sure Use Relative References is checked]
2. When done recording -> View -> Macros -> Stop Recording
3. View -> View Macros -> Run

# Combine text using Flash Fill  
```
Ex:: 
Column  A           B          C
        Cody       Chen      Cody Chen
        ...        ...       Cody Chen
        ...        ...       Cody Chen
```
1. Fill the entire row with how you want to combine
2. Then click on Flash Fill like below  
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Excel%20Flash%20Fill.png)

# Convert Date to Year
1. =CONVERT(number, from_unit, to unit)
- number = cells to be converted
- from_unit = "day"
- to unit = "yr"
  
# Week End Date (Assume 1st row of the date column is D2) 
https://www.youtube.com/watch?v=XG1kmcMg4A8  
1. (Sat-Fri) Week End Friday  
   =D2+(7-WEEKDAY(D2,16))
- (Mon-Sun) Week End Sunday   
   =D2+(7-WEEKDAY(D2,2))
2. Create Pivot Table -> Drag all the columns you want to rows, measure value to value field.
3. Click on any cell on the pivot table -> Design -> Report Layout -> Show in Tabular Form
4. Click on any cell on the pivot table -> Design -> Report Layout -> Repeat Item Labels
5. Click on any cell on the pivot table -> Design -> Subtotals -> Do not show subtotals
6. Click on any cell on the pivot table -> Design -> Grand Totals -> off for rows and columns
7. Click on any cell in the date column value, ungroup

# Groupby Rows in Pivot Table
1. Create Pivot Table
2. Click on any cell on the pivot table -> Design -> Report Layout -> Show in Tabular Form
3. Hold down ctrl key, and mouse left click to select the rows you want to groupby
4. Right Click -> Group (You can change the name for the column and the group)
5. Right Click -> Expand/Collapse -> Collapse Entire Field. (To see the sum of those group)

# xlookup (default is exact match)
- lookup_value: what you looking for 
- lookup_array: where can you find the above value from (SQL: FROM TABLE) (Need to press F4)
- return_array: what do you want to get back? (Select column you want to return) (SQL: SELECT Statement: Final output you want to return) (Need to press F4)

# AutoFill (Double Click ⤷ doesn't work)
1. Select the entire column
2. Ctrl + D

# Clear all filters
1. Data -> Next to Filter (Clear)

# Can't paste values errors:
1. Resize Table Error (Can't move cells in a filtered range or table):
- Remove the table first by clicking anywhere inside the table to activate it.
- Table Design -> Convert to Range -> Insert -> Table
2. When trying to get rid of formula by re-paste:
- Make sure the filters are cleared: Data -> Next to Filter (Clear)
- Paste data to another sheet as value, then paste it back.
