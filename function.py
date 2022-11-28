import matplotlib.pyplot as plt

squars = [1, 4, 9, 16, 25]
plt.plot(squars, linewidth=5)
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squars, linewidth=5)
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
