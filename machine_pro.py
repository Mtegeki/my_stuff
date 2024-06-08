import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
#from sklearn.utils import shuffle

data_f = pd.read_csv("student-mat.csv", sep=";")
data_f = data_f[["G1", "G2", "G3", "absences", "studytime", "failures"]]

predict = "G3"

X = np.array(data_f.drop([predict], axis=1))
Y = np.array(data_f[predict])
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.2)
model = linear_model.LinearRegression()
model.fit(X_train, Y_train)
accurace = model.score(X_test, Y_test)
print(accurace)
print(f"coefficient: \n {model.coef_}")
print(f"Intercept: \n {model.intercept_}")
prediction = model.predict(X_test)
for x in range(len(prediction)):
    print(f"prediction {prediction[x]} data used to predition {X_test[x]}  actualy value {Y_test[x]}")