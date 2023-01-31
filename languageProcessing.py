from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import os

path = "/Users/munkhchuulgaenkhbayar/Documents/Machine Learning/Items"

# Read data from csv
pathname = os.path.join(path, "Book1.csv")
data = pd.read_csv(pathname)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data.drop("column1", axis=1), data["column1"], test_size=0.2)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model on test set
score = model.score(X_test, y_test)
print("Test score: ", score)
