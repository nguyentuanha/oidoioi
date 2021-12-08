
import matplotlib.pyplot as plt
import numpy as np
divisions = ["div-a","div-b","div-c","div-d","div-e"]
division_average_marks=[70,82,62,65,68]
plt.bar(divisions, division_average_marks,color='green')
plt.title("bar graph")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.show()