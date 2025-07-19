import matplotlib.pyplot as plt
st = [20,25,24,27]
cls = ['12 A','12 B','12 C','12 D']
plt.plot(st,cls)
plt.xlabel('Number of Students')
plt.ylabel('Number of Sections')
plt.title("Students enrolled in Class 12")
plt.show()