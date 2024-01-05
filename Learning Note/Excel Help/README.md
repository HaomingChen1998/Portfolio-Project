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
   
# Macro
1. Select range to last row/column
```
Option Explicit

' Description: Tests the custom made Find functions in this module.
' Worksheet: DataJagged
' YouTube video: https://youtu.be/DpwAO5qnvAQ
' ExcelMacroMastery.com
Sub TestFind()

    ' Print the range address,last cell address, row and column to Immediate Window(Ctrl + G)
    Debug.Print "Last row is " & FindLastRow(shJagged.Cells)
    Debug.Print "Last column is " & FindLastcolumn(shJagged.Cells)
    
    Debug.Print "Last cell is: " & FindLastCell(shJagged.Cells).Address
    Debug.Print "The full range is: " & BuildRangeToLastCell(shJagged.Cells).Address
    
End Sub

' Description: Finds the last cell in a given range or worksheet.
' YouTube video: https://youtu.be/DpwAO5qnvAQ
' ExcelMacroMastery.com
Function FindLastCell(rg As Range) As Range
    
    On Error GoTo eh
    Dim lastRow As Long, lastColumn As Long
    
    lastRow = rg.Find("*", , Lookat:=xlPart, LookIn:=xlFormulas _
            , searchorder:=xlByRows, searchdirection:=xlPrevious).Row
    lastColumn = rg.Find("*", , Lookat:=xlPart, LookIn:=xlFormulas _
            , searchorder:=xlByColumns, searchdirection:=xlPrevious).Column

    Set FindLastCell = rg.Parent.Cells(lastRow, lastColumn)
Exit Function
eh:
   If Err.Number = 91 Then
        MsgBox "No data found for range [" & rg.Address & "]. Last cell will be set to first cell of range."
    End If
    Set FindLastCell = rg.Cells(1, 1)
End Function

' Description: Finds the last row in a given range or worksheet.
' YouTube video: https://youtu.be/DpwAO5qnvAQ
' ExcelMacroMastery.com
Function FindLastRow(rg As Range) As Long
    
    On Error GoTo eh
    
    FindLastRow = rg.Find("*", , Lookat:=xlPart, LookIn:=xlFormulas _
            , searchorder:=xlByRows, searchdirection:=xlPrevious).Row
Exit Function
eh:
   If Err.Number = 91 Then
        MsgBox "No data found for range [" & rg.Address & "]. Last row will be set to first row of range."
    End If
    FindLastRow = rg.Cells(1, 1).Row
End Function

' Description: Finds the last column in a given range or worksheet.
' YouTube video: https://youtu.be/DpwAO5qnvAQ
' ExcelMacroMastery.com
Function FindLastcolumn(rg As Range) As Long
        
    On Error GoTo eh
    
    FindLastcolumn = rg.Find("*", , Lookat:=xlPart, LookIn:=xlFormulas _
            , searchorder:=xlByColumns, searchdirection:=xlPrevious).Column

Exit Function
eh:
   If Err.Number = 91 Then
        MsgBox "No data found for range [" & rg.Address & "]. Last column will be set to first row of range."
    End If
    FindLastcolumn = rg.Cells(1, 1).Column
End Function


' Description: Builds a range based on the last row in a given range or worksheet.
' YouTube video: https://youtu.be/DpwAO5qnvAQ
' ExcelMacroMastery.com
Function BuildRangeToLastCell(rg As Range _
                    , Optional startRow As Long = 1 _
                    , Optional startcolumn As Long = 1) As Range
    
    ' Build the range from the first cell of the range(or based on the optional
    ' parameters) to the last cell found in the range.
    Set BuildRangeToLastCell = rg.Parent.Range( _
                            rg.Cells(startRow, startcolumn).Address _
                            , FindLastCell(rg).Address)

End Function
```

```
Sub DataPull_1()
'
' DataPull_1 Macro
'

'
    Sheets("new_data").Select
    Range("A2").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("Performance to Benchmark_110623").Select
    Range("A2").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    ActiveSheet.Paste
    Sheets("Pivot").Select
    Application.CutCopyMode = False
    ActiveSheet.PivotTables("PivotTable1").PivotCache.Refresh
    ActiveWorkbook.ShowPivotTableFieldList = True
    ActiveSheet.PivotTables("PivotTable1").PivotFields("Week End Date").AutoSort _
        xlAscending, "Week End Date"
    Sheets("Output").Select
    
    ActiveSheet.Range("$A$9:$O$436").AutoFilter Field:=5, Criteria1:= _
        "=CPC (w/o Dig Vid)", Operator:=xlOr, Criteria2:="=Media Cost (-dig vid)"
    Dim firstVisibleCell As Range
    Set firstVisibleCell = Range("F10:F436").SpecialCells(xlCellTypeVisible).Cells(1, 1)
    Range(firstVisibleCell, ActiveSheet.Cells.SpecialCells(xlCellTypeVisible).Cells.SpecialCells(xlLastCell)).Select
    Selection.NumberFormat = "$#,##0.00"
    
    ActiveSheet.Range("$A$9:$O$436").AutoFilter Field:=5, Criteria1:= _
        "=CTR (w/o Dig Vid)", Operator:=xlOr, Criteria2:="=VCR"
    Set firstVisibleCell = Range("F10:F436").SpecialCells(xlCellTypeVisible).Cells(1, 1)
    Range(firstVisibleCell, ActiveSheet.Cells.SpecialCells(xlCellTypeVisible).Cells.SpecialCells(xlLastCell)).Select
    Selection.NumberFormat = "0.00%"
    
    ActiveSheet.Range("$A$9:$O$436").AutoFilter Field:=5
    
    Range("A9").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("Last Weeks Data").Select
    Range("HistoricalData[[#Headers],[Campaign Brand]]").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    ActiveSheet.Paste
    Sheets("Pivot").Select
    
    Range("A4").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("Output").Select
    Range("A9").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    ActiveSheet.Paste
    
    Sheets("Output").Select

    ActiveSheet.Range("$A$9:$O$436").AutoFilter Field:=5, Criteria1:= _
        "=CPC (w/o Dig Vid)", Operator:=xlOr, Criteria2:="=Media Cost (-dig vid)"
    Set firstVisibleCell = Range("F10:F436").SpecialCells(xlCellTypeVisible).Cells(1, 1)
    Range(firstVisibleCell, ActiveSheet.Cells.SpecialCells(xlCellTypeVisible).Cells.SpecialCells(xlLastCell)).Select
    Selection.NumberFormat = "$#,##0.00"
    
    ActiveSheet.Range("$A$9:$O$436").AutoFilter Field:=5, Criteria1:= _
        "=CTR (w/o Dig Vid)", Operator:=xlOr, Criteria2:="=VCR"
    Set firstVisibleCell = Range("F10:F436").SpecialCells(xlCellTypeVisible).Cells(1, 1)
    Range(firstVisibleCell, ActiveSheet.Cells.SpecialCells(xlCellTypeVisible).Cells.SpecialCells(xlLastCell)).Select
    Selection.NumberFormat = "0.00%"
    
    ActiveSheet.Range("$A$9:$O$436").AutoFilter Field:=5
    
    Sheets("Pivot").Select
End Sub

```
