
from pylab import * 
import matplotlib.pyplot as plt
import numpy as np


MATRIX = [['ENGINESIZE','CO2EMISSIONS'],
		  [2.0         ,           196],
		  [2.4         ,           221],
		  [1.5         ,           136],
		  [3.5         ,           255],
		  [3.5         ,           244],
		  [3.5         ,           230],
		  [2.1         ,           197],
		  [2.3         ,           224],
		  [1.5         ,           138],
		  [3.3         ,           251],
		  [3.5         ,           247],
		  [3.4         ,           238],
		  [3.5         ,           234],
		  [3.7         ,           257],
		  [3.5         ,           232],
		  [3.7         ,           255],
		  [3.7         ,           237]]


class LinealRegression():
	def __init__(self):
		self.THETA1 = None
		self.THETA0 = None
		self.values1 = []
		self.values2 = []

	def __P(self, x, y, Color = 'blue'):
		a, = [x]
		b, = [y]
		plt.scatter(x, y, color= Color)

	def constructor(self, MATRIX):

		for i in range(len(MATRIX)):
			self.values1.append(MATRIX[i][0])
		self.values1.pop(0)


		for i in range(len(MATRIX)):
			self.values2.append(MATRIX[i][1])
		self.values2.pop(0)

		self.__P(self.values1,self.values2)

	def train(self, a, b):
		XMEDIA = 0
		YMEDIA = 0
		for i in a:
			XMEDIA = XMEDIA + i
			YMEDIA = YMEDIA + b[a.index(i)]
		XMEDIA = XMEDIA/len(a)
		YMEDIA = YMEDIA/len(b)



		DIVIDENDO = 0
		DIVISOR = 0
		for i in a:
			DIVIDENDO = DIVIDENDO + ((i - XMEDIA)*(b[a.index(i)] - YMEDIA))
			DIVISOR = DIVISOR + np.square((i - XMEDIA)) 

		self.THETA1 = DIVIDENDO/DIVISOR
		self.THETA0 = YMEDIA - self.THETA1*XMEDIA

	def show_graf(self, Color = 'green'):
		x = np.linspace(min(self.values1),max(self.values1), 100)
		y = self.THETA0 + self.THETA1*x
		plt.plot(x,y, color = Color) 
		

	def predict(self, num):
		return (self.THETA0 + self.THETA1*num)

	def evaluation(self, k_number):
		

		VAR1 = []
		VAR1.extend(self.values1)
		VAR2 = []
		VAR2.extend(self.values2)


		a = int(np.floor(len(VAR1)/k_number))

		X_TEST = VAR1[:a]
		Y_TEST = VAR2[:a]

		X_TRAIN = VAR1[a:]
		Y_TRAIN = VAR2[a:]
		self.show_graf()
		self.train(X_TRAIN, Y_TRAIN)

		

		SUM = 0
		for i in Y_TEST:
			print(i)
			print(X_TEST[Y_TEST.index(i)])
			print(self.predict(X_TEST[Y_TEST.index(i)]), '\n')
			SUM = SUM + (i - self.predict(X_TEST[Y_TEST.index(i)]))

		RESULT = SUM/k_number
		print(RESULT)
		self.show_graf('blue')
		plt.show()


	


		
		




		





LinealRegression = LinealRegression()





LinealRegression.constructor(MATRIX)
LinealRegression.train(LinealRegression.values1, LinealRegression.values2)
LinealRegression.evaluation(4)
































