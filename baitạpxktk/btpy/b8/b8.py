
import matplotlib.pyplot as plt
import numpy as np
divisions = ["div-a","div-b","div-c","div-d","div-e"]
girls_average_marks=[72,97,69,69,66]
boys_average_marks=[68,67,77,61,70]
index= np.arange(5)
width=0.30
plt.bar(index,boys_average_marks,width,color='green',label="boys marks")
plt.bar(index,girls_average_marks,width,color='blue',label="girls marks", bottom=boys_average_marks)
plt.title("bar graph")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.xticks(index,divisions)
plt.legend(loc='best')
plt.show()