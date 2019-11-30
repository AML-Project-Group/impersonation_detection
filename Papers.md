* Intrusion Detection in 802.11 (Kolias...) | 2015 | AWID-CLS-R | 4 classes | 155 and 20 features

Tried several algorithms first without feature selection (155) and then using 20 features manually selected. 
Using every features, the best result was with the J48 algorithm (based on the C4.5 decision tree) but takes long time, then the preferable ones are Random Forest and OneR.
Using 20 features, there is a small increase in the overall accuracy but a clear improvement in the training speed. The best algorithms are J48, Random Tree and then Random Forest.


* Deep abstraction and Weighted Feature Selection (Aminanto...) | 2017 | AWID-CLS-R | impersonation | 12-22 features

There are 2 steps: the feature extraction (unsupervised auto encoder) creates 50 features which are then added to the original features; the second step is the supervised feature selection, based on SVM, ANN and C4.5. The final detection accuracy for impersonation is 99.918%, the false alarm rate 0.012%

* DEMISe: Interpretable Deep Extraction and Mutual Information (Parker...) | 2019 | AWID-CLS-R | impersonation | 10 and 20 features

Two models are proposed: the common part is the Deep Extraction and Mutual Information Selection (DEMISe), where additional features are extracted using a two-layer deep-structured stacked encoder (SAE, used in the previous work). 
The DEMISe  is combined with a Radial Basis Function Classifier (DEMISe-RBFC, 20 features) and with a Tree Evaluation and Regression Detection (DETEReD, 10 features), using a C4.8 tree-based wrapper. 
The results are comparable to the previous paper, but the biggest improvement is in the build time, 72.14% and 52.29% faster
