<h1 align="center">Media Math</h1>

**<small>Cost Per Impression**<small>  
CPM = Cost / Impression

**<small>Cost Per Click**<small>  
CPC = Cost / Click

**<small>Click Through Rate**<small>  
CTR = Clicks / Impression

**<small>Video Complete Rate**<small>  
VCR = (View-throughs * 100) / Impressions  
OR     
VCR = (View-throughs / Impressions) * 100  
a “view through” typically refers to a viewer watching an entire video ad without skipping it


<h1 align="center">Workerbook Knowlege</h1>
  
**<small>25th, 50th, & 75th Percentiles**<small>  

1. Percentiles were calculated using OUTPUT tab which contains the new data, it calculates the percentile by each row, from column U to AD (the previous weekend friday date).
2. For this week's data, the 25th percentile is 354 means : For this week's data, 25% of the data would fall below the value 354 (ascending order)

**<small>v25, v50, & v75**<small>  
1. These v values are calculated by most_recent_week_data/corresponding_percentile.
- Ex: v25 is calculated by most_recent_week_data/25th percentile

1. Percentiles were calculated using OUTPUT tab which contains the new data, it calculates the percentile by each row, from column U to AD (the previous weekend friday date).
2. For this week's data, the 25th percentile is 354 means : For this week's data, 25% of the data would fall below the value 354 (ascending order)

<h1 align="center">Data Anomaly Check</h1>

**<small>When does percentile indicate non-issue?**<small>  
When most recent week's data is significantly:
1. Higher than 25th & 50th, but lower than 75th. (still within normalized range)
2. Lower than 75th & 50th, but higher than 25th.
3. If all higher/lower, but relevant metrics from most recent week are small numbers, that may indiciate the ad is still in QA (Making sure the quality is good before release to the public)
- Ex: When most recent data for CTR is significantly higher than all percentiles: Check relevant metrics (clicks & Impression), if they are low, might indiciate QA.
4. Higher than 25th & 50th,  75th. (still within normalized range)
5. Lower than 75th & 50th, but higher than 25th.

