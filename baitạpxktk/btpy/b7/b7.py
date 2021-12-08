
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.defchararray import index
divisions = ["div-a","div-b","div-c","div-d","div-e"]
division_average_marks=[70,82,62,65,68]
boys_average_marks=[70,82,62,65,68]
index= np.arange(5)
width=0.30
plt.bar(index,division_average_marks,width,color='green',label="division marks")
plt.bar(index+width,division_average_marks,width,color='blue',label="boys marks")
plt.title("bar graph")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.xticks(index+width/2,divisions)
plt.legend(loc='best')
plt.show()