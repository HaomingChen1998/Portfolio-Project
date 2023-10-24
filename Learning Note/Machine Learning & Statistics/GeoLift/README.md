<h1 align="center">Geolift:</h1>

GeoLift uses columns like location, date, KPI to measure lift from marketing campaigns at a geographical level between test and control markets.  

  - https://facebookincubator.github.io/GeoLift/docs/GettingStarted/Walkthrough

  
**<small>Steps**<small>
1. 

**<small>Definition**<small>
- Carbon tax is introduced in 1990, and the gas consumption goes down after 1990. The question is if this decline is really because of the carbon tax?
1. Synthetic Control Methods (SCM): It helps you to understand if something causes something else. The average of similar states that fit the target state (NY) very well pretrend (before New York receives carbon tax), these similar states should not receive carbon tax after 1990 as well. Ex. New York introduced carbon tax, Norway is similar to NY, but didn't introduce carbonx tax. Then you compare this average with what has actually happened in New York. This average is the counterfactual.
  - https://www.youtube.com/watch?v=EGqrtpEXxaU
  - https://www.youtube.com/watch?v=wpUXJbWnfo8
2. Counterfactual: What would it happen without? Ex: what would have happen to gas consumption if NY didn't introduce carbon tax?
3. Causal Effect: The difference between gasoline consumption with tax and gasoline consumption without tax after treatment.
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/SCM.png)
4. Power Analysis: Statistical analysis that you should run before executing a test to set it up for success. Through Power Analysis, you can find the following:
    - The optimal number of test locations.
    - Best test duration.
    - Select the ideal test and control markets.
    - Get a good estimate of the budget needed to run the test.
    - Determine which is the Minimum Detectable Effect to obtain significant results.
    - Align expectations.
5. GeoLiftMarketSelection() : a function that find which are the best combinations of test and control locations for the experiment.
My understanding of the difference between correlation and dtw:

Correlation: You listen to two songs are the same, but one song plays 5 seconds later. When you listen to them, they sound different.  

DTW: You listen to two songs are the same, and they play at the same time. When you listen to them, they sound the same.  

In the context of a retail industry, let's say a company runs an ad campaign about their tissue papers. It's relatively cheap, and it's for everyday use, so you can see the result faster. In this case, understanding the effective with a delay might not be important.  

In the context of a healthcare marketing campaign, let's say Pfizer runs an ad campaign about their new medicine, understanding the effectiveness with a delay might be important because healthcare decisions often take longer to decide. Ex: talking to their doctors first since no one medication works for all, consult insurance company about the cost, consult with family members if the cost is significant. If we do not use DTW in this case, we might conclude that the ad campaign wasn't effective at a city, but in fact, it is effective, but just with a delay.   
   
Dtw can also be used for anomaly detection (e.g. overlap time series between two disjoint time periods to understand if the shape has changed significantly, or to examine outliers)
