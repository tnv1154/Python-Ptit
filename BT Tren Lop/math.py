
import matplotlib.pyplot as plt


x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]
plt.style.use('seaborn-v0_8-muted')
fig, ax = plt.subplots()
ax.plot(x_value, y_value, 'b-')
ax.scatter(x_value, y_value,c="red", s= 100)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True, linestyle='-', alpha=0.7)  # Add grid lines with some transparency
plt.show()

a = [ [0 for x in range(10)] for y in range(10) ]
