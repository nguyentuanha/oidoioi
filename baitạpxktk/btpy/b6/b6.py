
import matplotlib.pyplot as plt
import numpy as np
divisions = ["div-a","div-b","div-c","div-d","div-e"]
division_average_marks=[70,82,73,65,68]
variance=[5,6,7,8,4]
plt.barh(divisions, division_average_marks,xerr=variance,color='green')
plt.title("bar graph")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.show()