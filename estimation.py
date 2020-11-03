import argparse
import numpy as np
from theta import theta0, theta1


def estimatePrice(value):
	return theta0 + theta1 * value


if (__name__ == '__main__'):
	parser = argparse.ArgumentParser(description="Price Estimation")
	parser.add_argument("number", help="number of kilometers", type=int)
	args = parser.parse_args()
	try:
		print(estimatePrice(args.number))
	except Exception as e:
		print(e)