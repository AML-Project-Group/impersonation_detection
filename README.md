# impersonation_detection


PLANNING (GROUP)

PRE-PROCESSING (INDIVIDUAL 1) - Michael

* The dataframe has many features with no values, then I used a for loop check the std for each columns: if the std == 0, then the feature is deleted. From the original 153 features we end up with 79.

* The class 155 is perfectly balanced: 50% with value 0, 50% with value 1

* The features have been sorted by correlation with the class, from the highest positive to the highest negative 

* The remaining 78 features have been subdivided into 4 groups on the basis of the correlation. We then have the original dataframe and 4 smaller dataframe: we could test each of them to see where we get the best results 

* In the first smaller dataframe, df20, none of the features has a normal form

* Tried to transform the data using normalisation, standardisation and also PowerTransformer, but there was no or just little improvement in the normal distribution

* Decided to binarise every non-binary features: not sure this is the best solution

* Binarised also the other dataframes, so now there are 10 dataframes to test: the original one, the 4 smaller ones and the binarised versions



SELECTING FEATURES (INDIVIDUAL 2)

* Conducted t-tests on the remaining features to see if any weren't varying significantly under the two classes

* Majority had extremely small p-values

* Used logistic regression as quick baseline

* Little value in selection by t-test p-value

* PCA much more productive. Logistic regression score of 97% on test data when using first 10 principal components

EXPLORING AND SELECTING ML ALGORITHMS (INDIVIDUAL 3) - Tim

REFINING ALGORITHMS (INDIVIDUAL 4)

EVALUATING MODEL AND ANALYSING THE RESULTS (INDIVIDUAL 5) - Mike

FUTURE WORK (GROUP)
