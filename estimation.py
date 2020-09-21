import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import theta
from loader import FileLoader

def estimatePrice(mileage):
		print(theta.theta0)
		return (theta.theta0 + (theta.theta1 * mileage))

loader = FileLoader()
data = loader.load("/Users/floblanc/Projects/AI/ft_linear_regression/data.csv")
#loader.display(data["price"],len(data))
x = np.array(data["km"])
print(x)
y = estimatePrice(x)#loader.internEstimatePrice(x)
print (y)
plt.scatter(data["km"], data["price"])
plt.plot(x,y, color='red')
plt.ylabel('price')
plt.xlabel('km')
plt.show()