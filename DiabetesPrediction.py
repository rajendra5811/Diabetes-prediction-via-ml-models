from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
import sys
import numpy as np
import pandas as pd

class Ui_Prediction(object):

    def browsefile_train(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select training File", "*.csv")
        print(fileName)
        self.lineEdit.setText(fileName)

    def browsefile_test(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select testing File", "*.csv")
        print(fileName)
        self.lineEdit_2.setText(fileName)

    def prediction(self):
        try:
            print("Prediction Starting..!")
            trainingset = self.lineEdit.text()
            testingset = self.lineEdit_2.text()

            if trainingset == "" or trainingset == "null" or testingset == "" or testingset == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                try:
                    df = pd.read_csv(trainingset)
                    X_train = np.array(df.drop(['Class'], 1))  # Train  DataSet
                    Y_train = np.array(df['Class'])  # Train Class

                    tf = pd.read_csv(testingset)
                    testdata = np.array(tf)
                    X_test = testdata.reshape(len(testdata), -1)
                    ann = RandomForestClassifier()  # MLPClassifier(); # Creation of ANN classifier
                    ann.fit(X_train, Y_train);  # fit ANN classifier on the training set
                    result = ann.predict(X_test)  # Prediction of ANN
                    print("Prediction Completed..!")
                    print(result)
                    if (result[0] == 1):
                        self.label_5.setText('POSITIVE')
                    else:
                        self.label_5.setText('NEGATIVE')


                except Exception as e:
                    print(e.args[0])
                    tb = sys.exc_info()[2]
                    print(tb.tb_lineno)



        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(727, 554)
        Dialog.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 40, 421, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Georgia\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 110, 241, 71))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"Georgia\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 160, 341, 41))
        self.lineEdit.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 160, 111, 41))
        self.pushButton.setStyleSheet("color: rgb(0, 85, 127);\n"
"\n"
"font: 14pt \"Georgia\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browsefile_train)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 380, 181, 41))
        self.pushButton_2.setStyleSheet("\n"
"font: 14pt \"Georgia\";\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.prediction)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 220, 251, 61))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 14pt \"Georgia\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 270, 341, 41))
        self.lineEdit_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 270, 111, 41))
        self.pushButton_3.setStyleSheet("color: rgb(0, 85, 127);\n"
"\n"
"font: 14pt \"Georgia\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.browsefile_test)


        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 470, 111, 71))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"Franklin Gothic Heavy\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(260, 470, 421, 71))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Georgia\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DIABETES PREDICTION "))
        self.label.setText(_translate("Dialog", "DIABETES PREDICTION "))
        self.label_2.setText(_translate("Dialog", "Training Dataset"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Prediction"))
        self.label_3.setText(_translate("Dialog", "Testing Dataset"))
        self.pushButton_3.setText(_translate("Dialog", "Browse"))

        self.label_4.setText(_translate("Dialog", "Result    :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Prediction()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
