import matplotlib.pyplot as plt
Month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
Units = [12,11,14,10,13,15,17,13,14,17,12,11]
plt.plot(Month,Units)
plt.xlabel("Months")
plt.ylabel("Units in lakhs")
plt.title("Month-wise Production")
plt.show()