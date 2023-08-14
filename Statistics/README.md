<h1 align="center">Supervised Learning vs Unsupervised Learning</h1>

1. **<small>Supervised Learning has both x / input and y / output**<small>
- It has two sub categories; Regression and Classification
- Regression Model: Linear Regression, Decision Tree, Random Forest, Neural Network
- Classification Model: Logistic Regression, Support Vector Machine, Naive Bayes, Decision Tree, Random Forest, Neural Network.

2. **<small>Unsupervised Learning has only x / input without y / output**<small>
- Infer patterns from input data without references to labeled outcomes.
- It has two sub categories, Clustering and Dimensionality Reduction
- Clustering Model: K-Means, Hierarchical, Mean Shift, Density-based
- Dimentionality Reduction (Feature Elimination/Extration): Principal Component Analysis(PCA) 

3. **<small>Reinforcement Learning: agent learning in interactive environment based on rewards and penalities.**<small>
- Giving reward to the computer, and letting it know what's something good that it should keep doing, and what's something bad, that it should stop doing.

<h1 align="center">Model Evaluation</h1>

**<small>Linear Regression:**<small>
  - R-Square (Coeff of Determination): goodness of fit
  - Adjusted R-Square: 40% means only 40% of the y variable are explained by the x variables. Meaning I need to add more correlated x variables to improve the model. If I added a new x variable, and I want to know if this new x variable is correlated to the y variable, I can compare the old adjusted r square with the new adjusted r square. If the new adjusted r square is higher, then it indicates there is correlation and more of y are explained by x variables. Note that correlation != casuation.
  - MAE (Mean Absolute Error): Sum of all resdiuals/error, and take the average by dividing all of the data points we have.
  - MSE (Mean Squared Error): Similar to MAE, but instead of absolute value, we squared it. It punishes large errors in the prediction, but it gets tricky to compare to y.
  - RMSE (Root Mean Squared Error): Take square root of MSE, so it punishes large errors in prediction, but also allow you to compare to y because they are in the same unit.
---  
    # MAE, MSE, MAE  
    from sklearn import metrics  
    print('MAE:', metrics.mean_absolute_error(y_test, prediction))  
    print('MSE:', metrics.mean_squared_error(y_test, prediction))  
    print('MAE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))  

    # R Squared  
    from sklearn.metrics import r2_score  
    r2 = r2_score(y_test, y_predict)  
    r2  

    # Adjusted R Squared  
    k = x_test.shape[1]  
    n = x_test.shape[0]  
    adj_r2 = 1-(1-r2)*(n-1)/(n-k-1)  
    adj_r2  
  
**<small>Logistic Regression:**<small>
1. Imagine you have class A for apples and class B for bananas. If your model avoid a lot of mistakes in predicting bananas as apples, then your model has high precision. If your model avoid lots of mistakes in predicting apples as bananas, then your model has a high recall. You want your model to aim high for both precision and recall. But if your model is really good at predicting one class, but sucks at predicting the other class, it would be misleading to look at them individually. F1 takes account both precision and recall, high F1 score means your model is doing a good job at predicting both apples and bananas.  
2. There might be some cases you might want to focus on precision over recall or vice versa. Imagine you have class A for aggressive cancer, class for no cancer. The stacks of misleading cancer for no cancer is high, so you want your model to avoid mistaking cancer as no cancer.
---  
Imagine you have 10 pictures and you want to predict which picture is dog, and which picture is not dog. Recall and Precision both have True Positive as numerator, the only difference is their denominator. Precision's denominator uses prediction as your base, and Recall's denominator uses truth as your base.
- Precision: out of 10 total pictures, your model predicted 7 pictures to be dog, but it turns out only 4 out of the 7 pictures are actually dog, this is true positive. Precision is 4/7.
- Recall: Think about truth as your base. Out of 10 total pictures, 6 of the pictures are dog. Out of those 6 pictures, 4 of them are actually dog. So recall is 4/6.
---  

- Precision: The proportion of positive identifications which were actually correct. Think about predictions as your base.
- Recall: The proportion of actual positives which were correctly classified. Think about truth as your base.
- F1 Score: A combination of precision and recall.
- Support: The number of samples each metric was calculated on.
- Accuracy: The accuracy of the model in decimal form.
`   # Accuracy Score
    from sklearn.metrics import accuracy_score  
    print('Accuracy Score: ', accuracy_score(y_test, y_pred))  

    # Confusion Matrix
    from sklearn.metrics import confusion_matrix  
    confusion_matrix(y_test, predictions)
    
    # Check Precision, Recall, and F1-score using classification report  
    from sklearn.metrics import classification_report  
    print(classification_report(y_test,predictions))
  `
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Statistics/Photo/Log%20Evaluation.png)

<h1 align="center">Save Created Model as a file</h1>

1. You don't want to re-run the model every time, so save it as a file using the following code:
---  

    # Export model as a file  
    from sklearn.externals import joblib  
    joblib.dump(created_model_name, 'new_file_name.joblib')  
    # Loading the model againc
    model = joblib.load('new_file_name.joblib'

<h1 align="center">Determining which model to use:</h1>
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
  - R-Square (Coeff of Determination): goodness of fit
  - Adjusted R-Square: 40% means only 40% of the y variable are explained by the x variables. Meaning I need to add more correlated x variables to improve the model. If I added a new x variable, and I want to know if this new x variable is correlated to the y variable, I can compare the old adjusted r square with the new adjusted r square. If the new adjusted r square is higher, then it indicates there is correlation and more of y are explained by x variables. Note that correlation != casuation.
  - MAE (Mean Absolute Error): Sum of all resdiuals/error, and take the average by dividing all of the data points we have.
  - MSE (Mean Squared Error): Similar to MAE, but instead of absolute value, we squared it. It punishes large errors in the prediction, but it gets tricky to compare to y.
  - RMSE (Root Mean Squared Error): Take square root of MSE, so it punishes large errors in prediction, but also allow you to compare to y because they are in the same unit.
4. Time Series problems: ARIMA, Prophet
