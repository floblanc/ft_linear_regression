import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from loader import FileLoader

class Trainer():
	def __init__(self):
		self.theta0 = 0
		self.theta1 = 0

	def internEstimatePrice(self, mileage):
		return (self.theta0 + (self.theta1 * mileage))

	def training(self, data):
		l0 = 0.5
		l1 = 0.0000000001
		som0 = 1 * len(data)
		som1 = 1 * len(data)
		index = 0
		while abs(som0 / len(data)) > 0.5 and abs(som1 / len(data)) > 0.5:
			x = np.array(data["km"])
			y = self.internEstimatePrice(x)
			plt.plot(x,y, color='green', zorder=1)
			plt.ylabel('price')
			plt.xlabel('km')
			som0 = 0
			som1 = 0
			for i in range(len(data)):
				som0 += self.internEstimatePrice(data["km"][i]) - data["price"][i]
				som1 += ((self.internEstimatePrice(data["km"][i]) - data["price"][i]) * data["km"][i])
			old0 = self.theta0
			old1 = self.theta1
			self.theta0 -= l0 * (som0 / len(data))
			self.theta1 -= l1 * (som1 / len(data))
			if ((self.theta0 >= 0) != (old0 >= 0)):
				l0 /= 2
			if ((self.theta1 >= 0) != (old1 >= 0)):
				l1 /= 2
			index += 1
		plt.scatter(data["km"], data["price"],  zorder=2)
		plt.plot(x,y, color='red')
		newFile = open("theta.py", "w+")
		newFile.write("theta0 = {}\ntheta1 = {}\n".format(self.theta0, self.theta1))
		newFile.close()
		plt.show()


file = "data.csv"
if (len(sys.argv) < 3):
	if (len(sys.argv) == 2):
		file = sys.argv[1]
	loader = FileLoader()
	path = sys.path[0]+ '/' + file
	data = loader.load(path)
	trainer = Trainer()
	trainer.training(data)
else:
	print("There is too much arguments.")