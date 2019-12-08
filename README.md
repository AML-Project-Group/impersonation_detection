# impersonation_detection


PLANNING (GROUP)

PRE-PROCESSING (INDIVIDUAL 1) - Michael

* The dataframe has many features with no values, then I used a for loop check the std for each columns: if the std == 0, then the feature is deleted. From the original 153 features we end up with 79.

* The class 155 is perfectly balanced: 50% with value 0, 50% with value 1

* After plotting the features, it's clear that none of them has a normal distribution. Most features are binary, having only the values 1 and 0

* Initially the features have been sorted by Pearson and by non-parametric correlations (Kendall and Spearman) but then this solution has been discarded. It has been created the file FeaturesByCorrelation.md for reference


* Tried to transform the data using normalisation, standardisation and also PowerTransformer, but there was no or just little improvement in the normal distribution

* Decided to binarise every non-binary features: not sure this is the best solution

* Now there are 2 dataframes available: df and df_binarized (having both 78 features + 1 class)

* Some features have duplicates, then they can be removed from the previous dataframes: the new dataframes have 65 and 36 features




SELECTING FEATURES (INDIVIDUAL 2) - Ian

* Conducted t-tests on the remaining features to see if any weren't varying significantly under the two classes

* Majority had extremely small p-values

* Some features are very sparse - consider eliminating them in preprocessing

* Used logistic regression as quick baseline using 60/40 split

* Evaluated using recall as metric - is this the most important to us?

* Combination of around 30 features with low p-value, some correlation with target, and healthy proportion of non-zero values achieves good recall

* So does first 10 or 20 principal components

* Some features already have only 2 values - consider treating these separately and standardising the others in preprocessing?

* Challenge is that it's quite easy to get 99%+ recall without careful feature selection on a train/test split of the training data, but this is not translating into high recall on the test data

* A good balance may be provided by a combination of A) five to ten features with high absolute value of kendal's rho with the target, B) five to ten features with highest mutual information and C) the first ten to twenty principle components

* Perhaps look into algorithms that are better at dealing with difficult/resistant cases - boosting for example - as this could give better performance on the test data

* `feature selection with dataframe generator` has preprocessing steps and feature selection based on four criteria
 * first n principal components (highly correlated features already removed)
 * high absolute pearson
 * high absolute kendall
 * high mutual information

* now removes highly correlated continuous features, and nearly identical categorical features (Tim's def of categorical)

* the function `get_df` returns a dataframe with selected features for further use

* TODO add chi2 threshold for selection, (although I'm not sure MI will miss anything that chi2 would pick up?)

* TODO add randomforest importance measure

EXPLORING AND SELECTING ML ALGORITHMS (INDIVIDUAL 3) - Tim


* Used the data set containing 79 columns.

* Create Randomforest model including bagging, with 100 tree. Results provied extremely accurate (split train/test - 80/20%)

* Limited the RandomForest to three layers. Results significantly reduced.

* In both cases, there are no real node importances that stand out. Some nodes have 0 importance.

* Next steps would be to remove features with 0 importance in both trees, and re-run.

* NN with 5 layers (small), and 5 neuron per layer. In reality this is quite small. 

* Prediction results were pretty good.

* Next steps would be to try NN with more neurons (considering we hae 78 features, try 78), and more neuron layers.

FEATURE SELECTION:

* Completed Chi2 tests on categorical variables. Identified categorical variables with <6 unique values (Question: Is this correct?).

*TO DO: 

Feature Selection: Do PCA between continuous variables ONLY. This can reduce multicolinearity. Use reduced PCAs for continuous data. To feed into models.

Model evaluations: Use the p-value features < 0.05 from chi2, and the transformed continuous data from PCA above in Logistic Regression, RF and NN. 



REFINING ALGORITHMS (INDIVIDUAL 4) - Cosmin

EVALUATING MODEL AND ANALYSING THE RESULTS (INDIVIDUAL 5) - Mike

* Performance Measure (classification accuracy, regression, and clustering)
- Confusion matrix - Precision - Recall -Specificity - F1 score
-PR curve - ROC curve
* Cross Validation
* Testing Algorithms (Test Datasets)

FUTURE WORK (GROUP)
