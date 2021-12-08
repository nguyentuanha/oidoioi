import matplotlib.pyplot as plt
import numpy as np
x=np.arange(2,5)
y=x**4
plt.subplot(1,2,1)
plt.plot([1,2,3,4],[1,4,9,16],"go")
plt.title("First Plot")

plt.subplot(1,2,2)
plt.plot(x,y,"r^")
plt.title("2nd SubPlot")

plt.suptitle("My sub-plots")
plt.show()