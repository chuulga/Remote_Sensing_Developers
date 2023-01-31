import pandas as pd
import matplotlib.pyplot as plt
import os

# Read data from csv
path = "/Users/munkhchuulgaenkhbayar/Documents/Machine Learning/Items"

lastPath = os.path.join(path, "Book1.csv")
data = pd.read_csv(lastPath)

# Create a scatter plot of two columns
plt.scatter(data["column1"], data["column2"])
plt.xlabel("name")
plt.ylabel("column2")
plt.show()