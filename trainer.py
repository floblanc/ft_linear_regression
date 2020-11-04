import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class FileLoader():
	def load(self, path):
		try:
			data = pd.read_csv(path)
			print("Loading dataset of dimensions {} x {}".format(data.shape[0], data.shape[1]))
			return data
		except Exception:
			print("CSV reader failed on : {}".format(path))
			exit()

	def display(self, df, n):
		print(df[:n])


class LinearRegression():

	def __init__(self, data, iterations, learningRate):
		self.theta = np.zeros((1, 2))
		print(self.theta)
		self.learningRate = learningRate if learningRate is not None else 0.1
		self.m = data.shape[0]
		self.iterations = iterations if iterations is not None else 100
		self.km = np.zeros((self.m, 1))
		self.price = np.zeros((self.m, 1))
		self.cost_history = np.zeros(self.iterations)

	def estimatePrice(self, value):
		return np.dot(self.theta, value)

	def cost_fun(self, value):
		return (1 / (2 * self.m)) * sum(((self.estimatePrice(value) - self.price)**2)[0])

	def standardize(self, data):
		self.km = np.array([(data.km - np.mean(data.km)) / np.std(data.km)])
		self.price = np.array([(data.price - np.mean(data.price)) / np.std(data.price)])

	def destandardize(self, data, X):
		predictions = self.estimatePrice(X)[0] * np.std(data.price) + np.mean(data.price)
		self.theta[0][1] = (predictions[self.m - 1] - predictions[0]) / (data.km[self.m - 1] - data.km[0])
		self.theta[0][0] = predictions[0] - data.km[0] * self.theta[0][1]

	def training(self, data):
		self.standardize(data)
		print("Training with {} iterations".format(self.iterations))
		X = np.append(np.ones(self.km.shape), self.km, axis=0)
		print(X.T)
		for i in range(self.iterations):
			self.theta = self.theta - (1 / self.m) * self.learningRate * np.dot(X, (self.estimatePrice(X) - self.price).T).T
			self.cost_history[i] = self.cost_fun(X)
		self.destandardize(data, X)
		print("End of training")


if (__name__ == '__main__'):
	parser = argparse.ArgumentParser(description="Training Linear Regression")
	parser.add_argument("file", help="data_set")
	parser.add_argument("-i", "--iterations", help="nombre d'interations", metavar="n", type=int)
	parser.add_argument("-l", "--learningRate", help="learning rate", metavar="l", type=float)
	args = parser.parse_args()
	loader = FileLoader()
	data = loader.load(args.file)
	trainer = LinearRegression(data, args.iterations, args.learningRate)
	trainer.training(data)
	plt.title("Training Result")
	plt.ylabel('price')
	plt.xlabel('km')
	values = np.append(np.ones((1, len(data.km))), np.array([data.km]), axis=0)
	plt.plot(data.km, trainer.estimatePrice(values)[0], color='red')
	plt.scatter(data.km, data.price)
	plt.show()
	plt.title("Mean Square Error evolution")
	plt.ylabel('MSE value')
	plt.xlabel('Iterations')
	plt.plot(trainer.cost_history)
	plt.show()
	newFile = open("theta.py", "w+")
	print()
	newFile.write("theta0 = {}\ntheta1 = {}\n".format(trainer.theta[0][0], trainer.theta[0][1]))
	newFile.close()
