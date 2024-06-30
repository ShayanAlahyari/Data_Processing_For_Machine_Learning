import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(filepath_or_buffer='Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
