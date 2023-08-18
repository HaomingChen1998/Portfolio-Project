# Markdown
```
1. # for bold title
2. double space for new line
3. **text** for bold  
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
