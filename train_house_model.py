import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

input_data_set_name = input('Please enter location and file name of Trainign Data')

df = pd.read_csv(input_data_set_name)

X=[ i for i in df.columns.values if i not in ['Price','Address']]
y='Price'

X_train, X_test, y_train, y_test = train_test_split(df[X],df[y], test_size=0.3, random_state=2023)
machine = LinearRegression()
machine.fit(X_train,y_train)
import pickle
filename = input('Please enterpi model name and location to extract model')

pickle.dump(machine, open(filename, 'wb'))

