# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
###############################

# creating our dataset and creating matrix of features and the output column
dataset = pd.read_csv(filepath_or_buffer='Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
##################################

# handling missing data
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])
print(x)