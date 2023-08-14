<h1 align="center">Supervised Learning vs Unsupervised Learning</h1>

# Supervised Learning has both x / input and y / output
- It has two sub categories; Regression and Classification
- Regression Model: Linear Regression, Decision Tree, Random Forest, Neural Network
- Classification Model: Logistic Regression, Support Vector Machine, Naive Bayes, Decision Tree, Random Forest, Neural Network.

# Unsupervised Learning has only x / input without y / output
- Infer patterns from input data without references to labeled outcomes.
- It has two sub categories, Clustering and Dimensionality Reduction
- Clustering Model: K-Means, Hierarchical, Mean Shift, Density-based
- Dimentionality Reduction (Feature Elimination/Extration): Principal Component Analysis(PCA) 

# Reinforcement Learning: agent learning in interactive environment based on rewards and penalities.
- Giving reward to the computer, and letting it know what's something good that it should keep doing, and what's something bad, that it should stop doing.

# Determining which model to use:
1. Classification Problem: (Logistic regression, Support Vector Machines (SVM), Random Forest, Decision Tree, k-Nearest Neighbors/KNN):
- Seaborn -> pairplot  

    import seaborn as sns  
    sns.pairplot(df, hue='TARGET CLASS')
- If not overlapped too much, use Decision Tree for small dataset, Random Forest for large dataset (Non-linear Classification), these usually take longer time.
- If almost completely overlapped, then use KNN (Non-linear Classification), KNN takes less time.
- If not overlapping, and I can draw a stright line in between, then log regression (Linear classification)
2. Clustering problems: K-Means Clustering, Hierarchical Clustering
3. Regression problems: Linear Regression, Polynomial Regression, Random Forest, Decision Tree
  - Accuracy measured by following:
  - R-Square: goodness of fit
  - Adjusted R-Square: 40% means only 40% of the y variable are explained by the x variables. Meaning I need to add more correlated x variables to improve the model. If I added a new x variable, and I want to know if this new x variable is correlated to the y variable, I can compare the old adjusted r square with the new adjusted r square. If the new adjusted r square is higher, then it indicates there is correlation and more of y are explained by x variables. Note that correlation != casuation.
  - MAE:
  - MSE:
  - RMSE:
4. Time Series problems: ARIMA, Prophet

