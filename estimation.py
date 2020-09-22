import matplotlib.pyplot as plt
import numpy as np
import sys
import theta
from loader import FileLoader

def estimatePrice(mileage):
		return (theta.theta0 + (theta.theta1 * mileage))

if (len(sys.argv) < 3):
	file = "data.csv"
	if (len(sys.argv) == 2):
		file = sys.argv[1]
	loader = FileLoader()
	data = loader.load(sys.path[0] + "/" + file)
	x = np.array(data["km"])
	y = estimatePrice(x)
	plt.scatter(data["km"], data["price"])
	plt.plot(x,y, color='red')
	plt.ylabel('price')
	plt.xlabel('km')
	plt.show()
else:
	print("There is too much arguments.")