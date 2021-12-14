# moodulite jms importimine
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
# Andmebaasi laadimine
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
nimed = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
andmestik = read_csv(url, names=nimed)
# Valideerimisandmebaasi jagamine
massiiv = andmestik.values
X = massiiv[:,0:4]
y = massiiv[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
# Ennustamine valideerimisandmebaasi kohta
mudel = SVC(gamma='auto')
mudel.fit(X_train, Y_train)
ennustused = mudel.predict(X_validation)
# Ennustuste hindamine ja hindamise kasutajale näitamine
print(accuracy_score(Y_validation, ennustused))
print(confusion_matrix(Y_validation, ennustused))
print(classification_report(Y_validation, ennustused))