# moodulite jms importimine
import PySimpleGUI as sg
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
# Andmebaasi laadimine
database = 'heart.csv'
väärtused = ['Age', 'Sex', 'Chest pain type', 'Resting blood pressure', 'Max heart rate:', 'Exercised induced angina', 'Thal', 'Target']
andmestik = read_csv(database, names=väärtused)
# Valideerimisandmebaasi jagamine
massiiv = andmestik.values
X = massiiv[:,0:7]
y = massiiv[:,7]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
# Ennustamine valideerimisandmebaasi kohta
mudel = SVC(gamma='auto')
mudel.fit(X_train, Y_train)
# Ennustuste hindamine ja hindamise kasutajale näitamine
#kasutajaliides
sg.theme('DarkBlack')
paigutus = [[sg.Text('Age:'), sg.InputText()],
            [sg.Text('Sex(1-male, 0-female):'), sg.InputText()],
            [sg.Text('Chest pain type:'), sg.InputText()],
            [sg.Text('1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic')],
            [sg.Text('Resting blood pressure:'), sg.InputText()],
            [sg.Text('Max heart rate:'), sg.InputText()],
            [sg.Text('Exercise induced angina:'), sg.InputText()],
            [sg.Text('Thalassemia:'), sg.InputText()],
            [sg.Text('''Value 0: NULL, Value 1: fixed defect (no blood flow in some part of the heart), Value 2: normal blood flow, Value 3: reversible defect (a blood flow is observed but it is not normal)''')],
            [sg.Button('Close'), sg.Button('Confirm')]]

aken = sg.Window('Heart Attack Possibilty Calculator', layout=paigutus)

while True:
    event, sisend = aken.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    elif event == 'Confirm':
        aken.close()
        ennustus = mudel.predict([list(sisend.values())])
        print(int(ennustus))
        if int(ennustus) == 0:
            paigutus2 = [[sg.Text('no/low chance of heart attack')]]
        elif int(ennustus) == 1:
            paigutus2 = [[sg.Text('high chance of heart attack')]]
        aken = sg.Window('Heart Attack Possibilty Calculator', layout=paigutus2)
