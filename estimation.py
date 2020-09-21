import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import theta

def estimatePrice(mileage):
		print(theta.theta0)
		return (theta.theta0 + (theta.theta1 * mileage))
