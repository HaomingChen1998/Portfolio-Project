<h1 align="center">Supervised Learning vs Unsupervised Learning</h1>

1. **<small>Supervised Learning has both x / input and y / output**<small>
- It has two sub categories; Regression and Classification
- Regression Model: Linear Regression, Decision Tree, Random Forest, Neural Network
- Classification Model: Logistic Regression, Support Vector Machine, Naive Bayes, Decision Tree, Random Forest, Neural Network.

2. **<small>Unsupervised Learning has only x / input without y / output**<small>
- Infer patterns from input data without references to labeled outcomes.
- You do not use training and testing.
- It has two sub categories, Clustering and Dimensionality Reduction
- Clustering Model: K-Means, Hierarchical, Mean Shift, Density-based
- Dimentionality Reduction (Feature Elimination/Extration): Principal Component Analysis(PCA) 

3. **<small>Reinforcement Learning: agent learning in interactive environment based on rewards and penalities.**<small>
- Giving reward to the computer, and letting it know what's something good that it should keep doing, and what's something bad, that it should stop doing.

<h1 align="center">Model Evaluation</h1>

**<small>Linear Regression:**<small>
  - R-Square (Coeff of Determination): goodness of fit
  - Adjusted R-Square: 40% means only 40% of the y variable are explained by the x variables. Meaning I need to add more correlated x variables to improve the model. If I added a new x variable, and I want to know if this new x variable is correlated to the y variable, I can compare the old adjusted r square with the new adjusted r square. If the new adjusted r square is higher, then it indicates there is correlation and more of y are explained by x variables. Note that correlation != casuation.
  - MAE (Mean Absolute Error): Sum of all residuals/error, and take the average by dividing all of the data points we have.
  - MSE (Mean Squared Error): Similar to MAE, but instead of absolute value, we squared it. It punishes large errors in the prediction, but it gets tricky to compare to y.
  - RMSE (Root Mean Squared Error): Take square root of MSE, so it punishes large errors in prediction, but also allow you to compare to y because they are in the same unit. A RMSE of $10 is fantastic for predicting the price of a house, but horrible for predicting the price of a candy bar!
```
# MAE, MSE, RMSE  
from sklearn import metrics  
print('MAE:', metrics.mean_absolute_error(y_test, prediction))  
print('MSE:', metrics.mean_squared_error(y_test, prediction))  
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))  

# R Squared  
from sklearn.metrics import r2_score  
r2 = r2_score(y_test, y_predict)  
r2  

# Adjusted R Squared  
k = x_test.shape[1]  
n = x_test.shape[0]  
adj_r2 = 1-(1-r2)*(n-1)/(n-k-1)  
adj_r2  
```

**<small>Classification:**<small>
1. Imagine you have class A for apples and class B for bananas. If your model avoid a lot of mistakes in predicting bananas as apples, then your model has high precision. If your model avoid lots of mistakes in predicting apples as bananas, then your model has a high recall. You want your model to aim high for both precision and recall. But if your model is really good at predicting one class, but sucks at predicting the other class, it would be misleading to look at them individually. F1 takes account both precision and recall, high F1 score means your model is doing a good job at predicting both apples and bananas.  
2. There might be some cases you might want to focus on precision over recall or vice versa. Imagine you have class A for aggressive cancer, class for no cancer. The stacks of misleading cancer for no cancer is high, so you want your model to avoid mistaking cancer as no cancer.
---  
Imagine you have 10 pictures and you want to predict which picture is dog, and which picture is not dog. Recall and Precision both have True Positive as numerator, the only difference is their denominator. Precision's denominator uses prediction as your base, and Recall's denominator uses truth as your base.
- Precision: out of 10 total pictures, your model predicted 7 pictures to be dog, but it turns out only 4 out of the 7 pictures are actually dog, this is true positive. Precision is 4/7.
- Recall: Think about truth as your base. Out of 10 total pictures, 6 of the pictures are dog. Out of those 6 pictures, 4 of them are actually dog. So recall is 4/6.
---  
https://www.youtube.com/watch?v=85dtiMz9tSo
- True Positive (TP): We correctly predicted that they do have disease.
- True Negative (TN): We correctly predicted that they don't have disease.
- False Positive (FP): We incorrectly predicted that they do have disease. (Type 1 error)
- False Negative (FN): We incorrectly predicted that they don't have disease. (Type 2 error)  

```
- false positive (precision) VS false negative (recall) in terms of disease
- falsely predicted disease VS falsely predicted no disease, which is more costly?
- I should focus on having a high Recall, because if you falsely predicted someone who has disease as no disease,
then this patient won't be treated on time. It's more costly.
```
 
- Precision: When your false positive (falsely predicted positive) is more costly, increase precision. When a positive value is predicted, how often is the prediction correct? The proportion of positive identifications which were actually correct. Think about predictions as your base. Ex: Focus on Precision for Spam Filter because spam goes to the inbox are more acceptable than non-spam is caught by the spam filter.
- Recall (Sensitivity): When false negative (falsely predicted negative) is more costly, increase recall. When the actual value is positive, how often is the prediction correct? The proportion of actual positives which were correctly classified. Think about truth as your base. Ex: Focus on Recall for Fraudulent Transaction Detector because normal transactions that are flagged as possible fraud are more acceptable than fraudulent transactions that are not detected. Another example is disease, you should increase recall.
- F1 Score: A combination of precision and recall. Consider this when you have an imbalanced dataset
- Support: The number of samples each metric was calculated on.
- Accuracy: The accuracy of the model in decimal form, only good with balanced classes.
```
# Accuracy Score
from sklearn.metrics import accuracy_score  
print('Accuracy Score: ', accuracy_score(y_test, y_pred))  

# Confusion Matrix
from sklearn.metrics import confusion_matrix  
confusion_matrix(y_test, predictions)

# Check Precision, Recall, and F1-score using classification report  
from sklearn.metrics import classification_report  
print(classification_report(y_test,predictions))

from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred_logreg))
print("Precision",metrics.precision_score(y_test,y_pred_logreg))
print("Recall",metrics.recall_score(y_test,y_pred_logreg))
print("f1_score",metrics.f1_score(y_test,y_pred_logreg))
```

- Adjust the threshold to increase/decrease recall/precision
https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Machine%20Learning%20%26%20Statistics/09_classification_metrics.ipynb

```
# Import and fit model, use the renamed model name for y_prob.
from sklearn.model_selection import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Get the probabilities of the prediction
y_prob = lr.predict_proba(X_test)[:, 1]
```

```
# Get the probabilities of the prediction
# Higher threshold increases precision, lower threshold increases recall.
y_new_pred = []
threshold = 0.8

for i in range(0, len(y_prob)):
  if y_prob[i] > threshold:
    y_new_pred.append(1)
  else:
    y_new_pred.append(0)

# Check the effect of probability threshold on predictions
cr2 = classification_report(y_test, y_new_pred)
print(cr2)
```

```
# Get the AUC and plot the curve
from sklearn.metrics import roc_curve, roc_auc_score
fpr, tpr, threshold = roc_curve(y_test, y_prob)
AUC = roc_auc_score(y_test, y_prob)

import matplotlib.pyplot as plt
plt.plot(fpr, tpr, linewidth=4)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.grid()
```

![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Log%20Evaluation.png)
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Confusion%20Matrix.png)

<h1 align="center">Save Created Model as a file</h1>

1. You don't want to re-run the model every time, so save it as a file using the following code:
```
# Export model as a file  
from sklearn.externals import joblib  
joblib.dump(created_model_name, 'new_file_name.joblib')
 
# Loading the model again
model = joblib.load('new_file_name.joblib')
```

<h1 align="center">Determining which model to use:</h1>

1. Classification Problem: (Logistic regression, Support Vector Machines (SVM), Random Forest, Decision Tree, k-Nearest Neighbors/KNN):
- Seaborn -> pairplot  
```
import seaborn as sns  
sns.pairplot(df, hue='TARGET CLASS')
```
- If not overlapped too much, use Decision Tree for small dataset, Random Forest for large dataset (Non-linear Classification), these usually take longer time.
- If almost completely overlapped, then use KNN (Non-linear Classification), KNN takes less time.
- If not overlapping, and I can draw a stright line in between, then log regression (Linear classification)
2. Clustering problems: K-Means Clustering, Hierarchical Clustering
3. Regression problems: Linear Regression, Polynomial Regression, Random Forest, Decision Tree
4. Time Series problems: ARIMA, Prophet

<h1 align="center">Model Definition:</h1>

1. **<small>KNN (K-Nearest Neighbors) for Classification**<small>
- A supervised machine learning that classifies the new data or case based on a similarity measure. It is mostly used to classifies a data point based on how its neighbours are classified. It looks at what's around you, and take the label of the majority that's around you.
- K stands for how many neighbors do we use to judge what the label is. Usually we use 3 or 5 for k.  
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/KNN.png)
2. **<small>Naive Bayes for Classification**<small>
-  It describes the probability of an event occurring based on prior knowledge of conditions that might be related to the event. We assume the features are independent of each other which simplifies the calculations, making it a fast and efficient algorithm.
- By ignoring relationships among words, it has high bias. Since it works well in practice, it has low variance. It's often used in identifing Spam vs Normal messages.
3. **<small>Logistic Regression for Classification**<small>
- Used for binary classification problems, where the goal is to predict a binary outcome (e.g. yes or no, true or false, 0 or 1) based on a set of input features. It works by modeling the probability of the binary outcome as a function of the input features using a logistic function, which maps any input value to a value between 0 and 1.
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/Log.png)  
4. **<small>SVM (Support Vector Machines) for Classification**<small>
- Finding the optimal hyperplane (i.e. decision boundary) that separates the data into different classes. The hyperplane is chosen such that it maximizes the margin, which is the distance between the hyperplane and the closest data points from each class. SVM can be used for both linearly separable and non-linearly separable data by using different types of kernels that transform the data into a higher dimensional space where it can be linearly separated. SVM is a popular machine learning algorithm due to its ability to handle high-dimensional data, handle non-linear decision boundaries, and its ability to avoid overfitting.
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/SVM.png)
Different Dimensions:
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/SVM%20different%20dimension.png)
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/SVM%20Dimension.gif)  
5. **<small>K-Means Clustering for Classification (Unsupervised Learning without Label / y)**<small>
- Used for clustering data points into groups based on their similarity. The algorithm works by first randomly initializing K cluster centers, where K is the number of clusters desired. Then, for each data point, the algorithm assigns it to the nearest cluster center based on its distance to that center. After all data points are assigned to a cluster, the algorithm updates the cluster centers to be the mean of all the data points in that cluster. The algorithm then iteratively repeats this process of assigning data points to clusters and updating cluster centers until convergence is reached, where the assignment of data points to clusters no longer changes. The result is K clusters of data points that are similar to each other and dissimilar to data points in other clusters. K-means is commonly used for customer segmentation, image segmentation, and anomaly detection.  
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/K%20Means.gif)
6. **<small>PCA (Principal Component Analysis), (Unsupervised Learning without Label / y)**<small>
- It is a technique used for dimensionality reduction in machine learning. The goal of PCA is to reduce the number of features in a dataset while retaining as much of the variation in the data as possible.
- PCA works by identifying the directions in which the data varies the most, known as the principal components. It then projects the data onto these principal components, creating a new set of features that capture most of the variation in the original data. The new features are linear combinations of the original features, so they are uncorrelated with each other.
- When you have a lot of features and not that many rows of data, it can make sense to run PCA. I wouldn't run PCA by default because I'd rather see the contribution of each feature to the response variable before deciding if it makes sense to reduce dimensions, but if the features seem redundant or have high multicollinearity, then it may make sense to use PCA to reduce the number of dimensions. The results of PCA may also be hard to interpret if the features being grouped together are not particularly intuitive.
![App Screenshot](https://github.com/HaomingChen1998/Portfolio-Project/blob/main/Learning%20Note/Photo/PCA.gif)

<h1 align="center">A/B Testing:</h1>

**<small>Steps**<small>
1. Randomly break the experiment into 2 groups, the control group, and treatment/test group. The control group receives the old version, and the treatment/test group receives the new version.
2. At least run the A/B testing for 2 weeks to ensure it captures a full purchase cycle.

**<small>Definition**<small>
1. Baseline Conversion Rate %: Current Conversion Rate
2. Minimum Detectable Effect %: This is the expected change, has to be reasonable. The higher the value of minimum detectable effect, the less the traffic you will need.
3. Statistical Significance: measure the likelihood that the observed value is true and not by chance. 95% level means we are going to observe this result 95% of the time.

**<small>Problems with AB Testing**<small>
1. Setting up the experiment might be impossible.
2. Experiment takes too long, it makes more sense to use already exist data, this is call **<small>Casual Inference**<small>.

<h1 align="center">Casual Inference:</h1>

1. Confounders: A variable that is not included in an experiment, yet affects the relationship between both the independent and dependent variable in an experiment. This type of variable can mix the results of an experiment and lead to unreliable findings.
- Ex: Suppose a healthcare marketing campaign is promoting a new lung health supplement and uses data showing that individuals who consume the supplement have better lung health. However, if the majority of these individuals are non-smokers, smoking becomes a confounder. The improved lung health could be due to the absence of smoking rather than the supplement.
2. Counterfactual: What would it happen without? Ex: what would have happen to lung health if Pfizer didn't introduce their supplement?
3. Selection Bias: A bias introduced to the experiment, so the sample is not representative of the whole population.
- Ex: Suppose a healthcare marketing campaign is promoting a new fitness device and collects data on its effectiveness only from fitness enthusiasts or professional athletes. This would introduce a sampling bias, as these individuals are not representative of the general population.


<h1 align="center">Percentile:</h1>

  https://www.youtube.com/watch?v=7sJaRHF03K8    
  https://www.youtube.com/watch?v=MSQpvuPL2cw 

**<small>Calculation**<small>

1. Order all the values in the data set from smallest to largest.
2. Index = (total_number_of_values * percentile_in_decimal_form).
- Example:
  - If you have 10 pieces of data or values in the data set, number_of_values = 10.
  - If you want to find the 25th percentile, percentile_in_decimal_form = 0.25
3. If index is WHOLE number:
    - Count the values in your data until you reach the index.
    - The kth percentile is the average of that corresponding value in your data and the value that directly follows it.
4. If index is Decimal number:
    - Round it up to the nearest whole number.
    - Count the values in your data until you reach the index.
    - The corresponding value in your data set is the kth percentile.

**<small>Meaning**<small>

- 25th percentile means the values where 25% of the data is below that value.
- 75th percentile means the values where 75% of the data is below that value.  
- Calculation Example: number of data points * 0.75  
- 50th percentile is the same as medium    
