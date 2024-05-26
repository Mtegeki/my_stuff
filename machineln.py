import pandas as pd
import numpy as np 
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data_fr = pd.read_csv("student-mat.csv", sep=";")
data_fr2 = data_fr[["G1","G2","G3","absences","failures","studytime"]]
X = np.array(data_fr2.drop(["G3"], axis=1))
y = np.array(data_fr2["G3"])
X_train,X_test,y_train,y_test = sklearn.model_selection.train_test_split(X,y, random_state=20, test_size=0.2)
model = linear_model.LinearRegression()
model.fit(X_train, y_train)
acc = model.score(X_test,y_test)
#print(X.head())
#print(X.tail())
prediction = model.predict(X_test)
print('coeficient \n', model.coef_)
print('intercept \n', model.intercept_)
print("accuracy of you model is : ",acc)
for i in range(len(prediction)):
    print("predicted : ",prediction[i], "data used : ", X_test[i], "actually value is :", y_test[i])
