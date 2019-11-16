import csv
import numpy
import pandas as pd

# change the path with your local path
filename = r'C:\Users\user\jupyterSourceFiles\datasets\awid\train_imperson_without4n7_balanced_data.csv'

# create the dataframe
dfTrain = pd.read_csv(filename,
                      header=0,
                      na_values=['nan'])


# see dataframe info
dfTrain.head()
dfTrain.info()
dfTrain.describe()


# many attributes have no values, this code delete them from the dataframe
columnsToDelete = [] 

for key, value in dfTrain.iteritems():
    if sum(value) == 0:
        columnsToDelete.append(key)

dfTrain = dfTrain.drop(columnsToDelete, axis=1)

# use the following code if you want to test that the current attributes have some values
# dfTrain.sum(axis = 0, skipna = True)


# the observations are perfectly balanced: 50% class 0, 50% class 1 
class_counts = dfTrain.groupby('155').size()
class_counts

# show the 10 attributes with the highest positive correlations with the class
correlations = dfTrain.corr(method='pearson')
corr = correlations["155"].sort_values(ascending=False) # sort the correlations from highest to lowest
corr[0:10]

# The 80 columns are subdivided into 4 groups based on the correlation
# columns 17 and 139 have always value = 1, then they are excluded
# first 3 groups have 20 items, the last one has 18 items
HiCorr20 = ['71', '50', '68', '38', '73', '66', '140', '61', '142', '79', 
               '6', '5', '64', '80', '18', '20', '16', '26', '29', '43', '155']
HiCorr40 = ['89', '52', '15', '62', '14', '48', '111', '138', '133', '97', 
               '83', '105', '113', '88', '117', '84', '108', '86', '120', '78', '155']
LoCorr60 = ['119', '123', '144', '106', '72', '98', '90', '125', '118', '112', 
               '93', '109', '104', '121', '143', '76', '141', '128', '127', '129', '155']
LoCorr80 = ['130', '126', '107', '94', '122', '77', '110', '70', '75', '154', 
               '9', '8', '145', '146', '82', '47', '51', '67', '155']


# create 4 smaller dataframes
dfTrain20 = dfTrain[HiCorr20]
dfTrain40 = dfTrain[HiCorr40]
dfTrain60 = dfTrain[LoCorr60]
dfTrain80 = dfTrain[LoCorr80]

# analyze the first dataframe
skew = dfTrain20.skew()
skew










