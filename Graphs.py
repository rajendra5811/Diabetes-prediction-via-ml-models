import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import sys

def view(rlist):
    height=rlist
    bars = ('DT','ANN','NB','SVM','RF')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=['red','green','blue','maroon','indigo'])
    plt.xticks(y_pos, bars)
    plt.xlabel('Algorithms')
    plt.ylabel('Accuracy')
    plt.title('Prediction Accuracy Analysis')
    plt.show()


