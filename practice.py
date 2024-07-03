# importing libraries
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
###############################

# creating our dataset and creating matrix of features and the output column
dataset = pd.read_csv(filepath_or_buffer='Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
##################################

# handling missing data

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

###################

# Handling categorical data

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

le = LabelEncoder()
y = le.fit_transform(y)

###########


# Splitting dataset into training set and test set before feature scaling

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

################


### Feature scaling

sc = StandardScaler()
