import matplotlib.pyplot as plt
import numpy as np

divisons = ["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisons_average_marks = [50, 60, 80, 70, 40]

plt.bar(divisons, divisons_average_marks, color='pink')
plt.title("Bar Graph")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.show()