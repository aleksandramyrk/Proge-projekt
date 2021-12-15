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
paigutus = [[sg.Text('Age:', font=('Ariel', 11), size=(20, 1)), sg.InputText()],
            [sg.Text('Sex:', font=('Ariel', 11), size=(20, 1)), sg.InputText()],
            [sg.Text('', size=(22, 1)), sg.Text('1-male; 0-female', font=('Ariel', 11))],
            [sg.Text('Chest pain type:', font=('Ariel', 11), size=(20, 1)), sg.InputText()],
            [sg.Text('', size=(22, 1)), sg.Text('1-typical angina; 2-atypical angina; 3-non-anginal pain; 4-asymptomatic', font=('Ariel', 11))],
            [sg.Text('Resting blood pressure:', font=('Ariel', 11), size=(20, 1)), sg.InputText()],
            [sg.Text('Max heart rate:', font=('Ariel', 11), size=(20, 1)), sg.InputText()],
            [sg.Text('Exercise induced angina:', font=('Ariel', 11), size=(20, 1)), sg.InputText()],
            [sg.Text('Thalassemia:', font=('Ariel', 11), size=(20, 1)), sg.InputText()],
            [sg.Text('', size=(22, 1)), sg.Text('0-NULL; 1-fixed defect (no blood flow in some part of the heart); 2-normal blood flow;', font=('Ariel', 11))],
            [sg.Text('', size=(22, 1)), sg.Text('3-reversible defect (a blood flow is observed but it is not normal', font=('Ariel', 11))],
            [sg.Button('Close', font=('Ariel', 11)), sg.Button('Confirm', font=('Ariel', 11))]]

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
            paigutus2 = [[sg.Text('')],
                        [sg.Text('No/low chance of heart attack.', font=('Ariel', 16), justification='center', size=(100, 1))]]
        elif int(ennustus) == 1:
            paigutus2 = [[sg.Text('')],
                        [sg.Text('High chance of heart attack.', font=('Ariel', 16), justification='center', size=(100, 1))]]
        aken = sg.Window('Heart Attack Possibilty Calculator', layout=paigutus2, size=(400, 100))
