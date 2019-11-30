I used seed 7 and split ratio = 0.33 
Avoided LOOCV because computationally heavy and the metric Logarithmic Loss because not easy to understand
Feel free to add columns 

|   Features    | Feature Selection | Algorithm  | k-fold (5)  | k-fold (10)  | k-fold (20)  | Split Train/Test + AUC | Split Train/Test + ConfMatr | 
| ------------- |:-------------:| -----:| -----:| -----:| -----:| -----:| -----:|
|	10	|	UST (Chi2)	|	Logistic Regr	| 93.301% | 93.447% | 94.678% | 0.994 | [[15567, 526], [715, 15217]] |