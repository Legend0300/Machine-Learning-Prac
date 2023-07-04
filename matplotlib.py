#Line plot

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()


# Scatter plot:

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()

#Histogram:
data = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6]
plt.hist(data, bins=5)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()



# Custom:
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
plt.plot(x, y, color='red', linestyle='--', marker='o', label='Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Plot')
plt.legend()
plt.grid(True)
plt.show()

