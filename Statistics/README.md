<h1 align="center">Machine Learning Model Usage</h1>

# Supervised Learning has both x / input and y / output
- It has two sub categories; Regression and Classification
- Regression Model: Linear Regression, Decision Tree, Random Forest, Neural Network
- Classification Model: Logistic Regression, Support Vector Machine, Naive Bayes, Decision Tree, Random Forest, Neural Network.

# Unsupervised Learning 
- Infer patterns from input data without references to labeled outcomes.
- It has two sub categories, Clustering and Dimensionality Reduction
- Clustering Model: K-Means, Hierarchical, Mean Shift, Density-based
- Dimentionality Reduction (Feature Elimination/Extration): Principal Component Analysis(PCA) 

# How to choose what ML to use?
1. Classification Problem:
- Seaborn -> pairplot
import seaborn as sns
sns.pairplot(df, hue='TARGET CLASS')
- If not overlapped too much, use Decision Tree for small dataset, Random Forest for large dataset (Non-linear Classification), these usually take longer time.
- If almost completely overlapped, then use KNN (Non-linear Classification), KNN takes less time.
- If not overlapping, and I can draw a stright line in between, then log regression (Linear classification)


# ML Categories
1. Classification problems: Logistic regression, Support Vector Machines (SVM), Random Forest, Decision Tree, k-Nearest Neighbors (KNN). These models are designed to classify data points into different categories or classes based on their features.
2. Clustering problems: K-Means Clustering, Hierarchical Clustering. These models are designed to group data points into clusters based on their similarity or distance from each other.
3. Regression problems: Linear Regression, Random Forest Regression, ARIMA. These models are designed to predict a continuous numerical value based on input variables.
4. Time Series problems: ARIMA, Prophet. These models are designed to forecast future values based on historical time series data.
