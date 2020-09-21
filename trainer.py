import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
		while abs(som0 / len(data)) > 0.5 and abs(som1 / len(data)) > 0.5:
			som0 = 0
			som1 = 0
			for i in range(len(data)):
				som0 += self.internEstimatePrice(data["km"][i]) - data["price"][i]
				som1 += ((self.internEstimatePrice(data["km"][i]) - data["price"][i]) * data["km"][i])
			#print("som0 = {} et som1 = {} et len(data) = {}".format(som0, som1, len(data)))
			old0 = self.theta0
			old1 = self.theta1
			self.theta0 -= l0 * (som0 / len(data))
			#print("diff = %f", som0 / len(data))
			self.theta1 -= l1 * (som1 / len(data))
			if ((self.theta0 >= 0) != (old0 >= 0)):
				l0 /= 2
			if ((self.theta1 >= 0) != (old1 >= 0)):
				l1 /= 2
			#print("t0 {} et t1 {}".format(self.theta0, self.theta1))
		print(self.theta0)
		print(self.theta1)
		newFile = open("theta.py", "w+")
		newFile.write("theta0 = {}\ntheta1 = {}\n".format(self.theta0, self.theta1))
		newFile.close()
		#theta.theta0 = self.theta0
		#theta.theta1 = self.theta1
		#theta.theta0 = 0
		#theta.theta1 = 0
		#modify_thetas(self.theta0, self.theta1)


loader = FileLoader()
data = loader.load("/Users/floblanc/Projects/AI/ft_linear_regression/data.csv")
#loader.display(data["price"],len(data))
trainer = Trainer()
trainer.training(data)