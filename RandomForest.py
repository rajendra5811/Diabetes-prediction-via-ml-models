
import numpy.random as numrandom
from Graphs import view
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import warnings
import sys
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

def classify_rf(datainput, y_class):
    data = []

    try:
        warnings.warn("Variables are collinear.")
        # Split data into Test & Training set where test data is 30% & training data is 70%
        x_train, x_test, y_train, y_test = train_test_split(datainput, y_class, test_size=0.3)

        clf_rf = RandomForestClassifier()
        clf_rf.fit(x_train, y_train)
        predicted_rf = clf_rf.predict(x_test)
        rf_ac = metrics.accuracy_score(y_test, predicted_rf) * 100
        list_rf = performance_metrics(y_test, predicted_rf,"RF")
        print(list_rf)
        print("The accuracy score using the RF is ->")
        print(rf_ac)
        return rf_ac,list_rf



    except Exception as e:
                print("Error=" + e.args[0])
                tb = sys.exc_info()[2]
                print(tb.tb_lineno)


def performance_metrics(y_test,predicted_class,alg):
    print('accuracy')
    #Accuracy = (TP + TN) / ALL
    accuracy=accuracy_score(y_test, predicted_class)*100
    print(accuracy_score(y_test,predicted_class))
    print('precision')
    # Precision = TP / (TP + FP) (Where TP = True Positive, TN = True Negative, FP = False Positive, FN = False Negative).
    precision=precision_score(y_test, predicted_class, pos_label=1)
    print(precision_score(y_test,predicted_class,pos_label=1))
    print('recall')
    #Recall = TP / (TP + FN)
    recall=recall_score(y_test, predicted_class, pos_label=1)
    print(recall_score(y_test,predicted_class,pos_label=1))
    print('f-Score')
    #F - scores are a statistical method for determining accuracy accounting for both precision and recall.
    fscore=f1_score(y_test, predicted_class, pos_label=1)
    print(f1_score(y_test,predicted_class,pos_label=1))
    list = []
    list.append(alg)
    list.append(str(accuracy))
    list.append(str(round(precision,2)))
    list.append(str(round(recall,2)))
    list.append(str((round(fscore,2))))
    list.append(str((round(fscore, 2))))

    return list




