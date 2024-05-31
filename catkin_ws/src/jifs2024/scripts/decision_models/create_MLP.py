import sys
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.neural_network import MLPClassifier
import pickle
import time
import statistics
    
datafile = "./train_fold_10.csv"
data = pd.read_csv(datafile)  
print(data)      

model = MLPClassifier(hidden_layer_sizes=(8,8,8), max_iter=500, activation='relu', solver='adam', random_state=125)
   #print(MLP_name, flush = True)

X_train = data.drop(['action'], axis = 1)
y_train = data['action']

print("X_train.head ", X_train.head(), flush = True)
print("X_train.info ", X_train.info(), flush = True)
print("X_train.describe ", X_train.describe(), flush = True)
print("X_train ", X_train.shape, flush = True)                  

start_time = time.time()
model.fit(X_train, y_train) 
end_time = time.time()

training_time = end_time - start_time
#print("Training time:", training_time, flush = True)

filename = "./MLP_10.mlp"
pickle.dump(model, open(filename, 'wb'))  




