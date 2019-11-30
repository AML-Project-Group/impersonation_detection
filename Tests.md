I used seed 7 and split ratio = 0.33, avoided LOOCV because computationally heavy and the metric Logarithmic Loss because not easy to understand

Feel free to add columns. LR = Logistic Regression, UST = Univariate Statistical Tests


|   Features    | Feature Selection | Algorithm  | k-fold5  | k-fold10  | k-fold20  | Split Train/Test + AUC | Split Train/Test + ConfMatr | 
| :-------------: |:-------------:| :-----:| :-----:| :-----:| :-----:| :-----:| :-----:|
|	10	|	UST (Chi2)	|	LR	| 93.301% | 93.447% | 94.678% | 0.994 | [[15567, 526], [715, 15217]] |
|	20	|	UST (Chi2)	|	LR	| 95.511% | 96.075% | 97.432% | 0.998 | [[15742, 351], [127, 15805]] |
|	30	|	UST (Chi2)	|	LR	| 93.611% | 94.219% | 96.800% | 0.999 | [[15817, 276], [44, 15888]] |
|	78	|	-	|	LR	| 93.978% | 94.724% | 97.094% | 0.999 | [[15874, 219], [44, 15888]] |