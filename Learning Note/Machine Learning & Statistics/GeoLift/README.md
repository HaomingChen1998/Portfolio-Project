<h1 align="center">Geolift:</h1>
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
