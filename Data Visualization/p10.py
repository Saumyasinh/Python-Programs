import matplotlib.pyplot as plt
data = {'Scratch':23, 'AI':17, 'Java':35, 'Python':29, 'PHP':12}
courses=list(data.keys())
values=list(data.values())
plt.bar(courses,values,color='blue',width=0.4)
plt.xlabel("Courses Offered")
plt.ylabel("No. of Students Enrolled")
plt.title("Students Enrolled in Different Courses")
plt.show()