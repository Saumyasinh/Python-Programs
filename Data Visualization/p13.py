import matplotlib.pyplot as plt
import numpy as np
a=np.array([10,30,5,42,55,54,11,20,51,15,75,37,25])
plt.hist(a,bins=[0,25,50,75,100])
plt.title("Marks obtained by Students in a Class")
plt.xticks([0,25,50,75,100])
plt.xlabel("Marks")
plt.ylabel('No. of students')
plt.show()