# impersonation_detection


PLANNING (GROUP)

PRE-PROCESSING (INDIVIDUAL 1) - Michael

* Note: locally I'm using Jupyter, but I'm pushing a .py file rather than an .ipynb because maybe someone else want to use another tool. In Jupyter I do not use the print statement, then you have to add it if necessary  

* The dataframe has many attributes with no values, then I used a for loop to sum the values for each columns: if the sum == 0, then the attibute is deleted. From the original 155 attributes we end up with 80.

* The class 155 is perfectly balanced: 50% with value 0, 50% with value 1

* The attributes have been sorted by correlation with the class, from the highest positive to the highest negative 

* Two attributes, 17 and 139, have always value 1, then they have been deleted as well

* The remaining 78 attributes have been subdivided into 4 groups on the basis of the correlation. We then have the original dataframe and 4 smaller dataframe: we could test each of them to see where we get the best results 

* In the first smaller dataframe, none of the attributes has a normal form

* This weekend I'm going to work on the data transformation, in particular the normalisation



SELECTING FEATURES (INDIVIDUAL 2)

* Conducted t-tests on the remaining features to see if any weren't varying significantly under the two classes

* Majority had extremely small p-values

* Used logistic regression as quick baseline

* Little value in selection by t-test p-value

* PCA much more productive. Logistic regression score of 97% on test data when using first 10 principal components

EXPLORING AND SELECTING ML ALGORITHMS (INDIVIDUAL 3)

REFINING ALGORITHMS (INDIVIDUAL 4)

EVALUATING MODEL AND ANALYSING THE RESULTS (INDIVIDUAL 5)

FUTURE WORK (GROUP)
