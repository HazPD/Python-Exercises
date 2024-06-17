import matplotlib.pyplot as plt

# Sample data
months = ['January', 'February', 'March', 'April', 'May']
sales = [10000, 12000, 9000, 11000, 10500]

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(months, sales, color='skyblue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)

# Display the plot
plt.show()
