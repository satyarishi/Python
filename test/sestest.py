'''abc = "With three words"
stuff = abc.split()
print(len(stuff))

String ='Python'
s1 = slice(3) 
s2 = slice(1, 5, 1)
  
print("String slicing")  
print(String[s1])  
print(String[s2])'''



pip install sklearn
import sklearn
from sklearn import tree
features = [[2,100],[6,25],[1,300],[1,1000],[4,100],[10,100]]
label = [1,2,1,1,2,2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,label)
print(clf.predict([[4,140]]))
