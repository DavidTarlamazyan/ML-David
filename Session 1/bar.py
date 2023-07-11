import matplotlib.pyplot as plt

products = ["Product1", "Product2", "Product3", "Product4"]
sales = [320, 240, 450, 520]

plt.bar(products, sales, color = ['red', 'blue', 'green', 'orange'])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data")
plt.legend(['Sales'])
plt.show()
