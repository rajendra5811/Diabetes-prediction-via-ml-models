from PyQt5 import QtCore, QtGui, QtWidgets
from Graphs import view
from DiabetesPrediction import Ui_Prediction
from ANN import classify_ann
from DecisionTree import classify_dt
from SVM import classify_svm
from NaiveBayes import classify_nb
from RandomForest import classify_rf
import sys
import numpy as np
import pandas as pd
from Results import Ui_Results
class Ui_AdminHome(object):


    def predicting(self):
        self.pre = QtWidgets.QDialog()
        self.ui = Ui_Prediction()
        self.ui.setupUi(self.pre)
        self.pre.show()

    def evaluation(self):

        datainput = pd.read_csv("trainingset.csv")
        y = datainput['Class']
        del datainput['Class']

        dt_ac, list_dt = classify_dt(datainput, y)
        ann_ac,list_nn= classify_ann(datainput,y)
        svm_ac, list_svm = classify_svm(datainput, y)
        nb_ac, list_nb = classify_nb(datainput, y)
        rf_ac, list_rf = classify_rf(datainput, y)

        list = []
        list.clear()
        list.append(dt_ac)
        list.append(ann_ac)
        list.append(nb_ac)
        list.append(svm_ac)
        list.append(rf_ac)
        view(list)
        data = []
        data.append(list_dt)
        data.append(list_nn)
        data.append(list_nb)
        data.append(list_svm)
        data.append(list_rf)

        self.res = QtWidgets.QDialog()
        self.ui = Ui_Results()
        self.ui.setupUi(self.res)
        self.ui.view(data)
        self.res.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(685, 400)
        Dialog.setStyleSheet("background-image: url(../Diabetes/images/dbts2.jpg);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 80, 271, 51))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Demi\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predicting)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 180, 271, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Demi\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.evaluation)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DIABETES PREDICTION"))
        self.pushButton.setText(_translate("Dialog", "Diabetes Prediction"))
        self.pushButton_2.setText(_translate("Dialog", "Classifications Performance"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdminHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

