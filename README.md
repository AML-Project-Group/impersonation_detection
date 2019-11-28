# impersonation_detection


PLANNING (GROUP)

PRE-PROCESSING (INDIVIDUAL 1) - Michael

* The dataframe has many features with no values, then I used a for loop check the std for each columns: if the std == 0, then the feature is deleted. From the original 153 features we end up with 79.

* The class 155 is perfectly balanced: 50% with value 0, 50% with value 1

* The features have been sorted by correlation (Pearson) with the class, from the highest positive to the highest negative 

* The remaining 78 features have been subdivided into 4 groups on the basis of the correlation. We then have the original dataframe and 4 smaller dataframe: we could test each of them to see where we get the best results 

* In the first smaller dataframe, df20, none of the features has a normal form

* When we have no normal distribution, it is possible to use non-parametric statistics like the Kendall and Spearman correlations. Compared to Pearson's, these two correlations show some differences. The file FeaturesByCorrelation.md shows a table with values for the 3 correlations (Pearson, Kendall, Spearman)

* Tried to transform the data using normalisation, standardisation and also PowerTransformer, but there was no or just little improvement in the normal distribution

* Decided to binarise every non-binary features: not sure this is the best solution

* Binarised also the other dataframes, so now there are 10 dataframes to test: the original one, the 4 smaller ones and the binarised versions

* After splitting the training set into 2 parts, some dataframes show good results (accuracy > 98%), but the best result is with the dataframe using the non-paramtric correlations: in particular the dataframe using the first 18 common features having the highest positive Kendall/Spearman correlation. Using only these 18 features the accuracy is 100% on the validation set



SELECTING FEATURES (INDIVIDUAL 2) - Ian

* Conducted t-tests on the remaining features to see if any weren't varying significantly under the two classes

* Majority had extremely small p-values

* Some features are very sparse - consider eliminating them in preprocessing

* Used logistic regression as quick baseline using 60/40 split

* Evaluated using recall as metric - is this the most important to us?

* Combination of around 30 features with low p-value, some correlation with target, and healthy proportion of non-zero values achieves good recall

* So does first 10 or 20 principal components

* Some features already have only 2 values - consider treating these separately and standardising the others in preprocessing?

* Challenge is that it's quite easy to get 99%+ recall with not very well chosen features on a train/test split of the training data, but this is not translating into high recall on the test data

EXPLORING AND SELECTING ML ALGORITHMS (INDIVIDUAL 3) - Tim

REFINING ALGORITHMS (INDIVIDUAL 4) - Cosmin

EVALUATING MODEL AND ANALYSING THE RESULTS (INDIVIDUAL 5) - Mike

FUTURE WORK (GROUP)
