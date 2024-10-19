import numpy as np

class Perceptron:
   def __init__(self, n_iterations, rate):
    self.rate = rate
    self.n_iterations = n_iterations
    self.weights = None
    self.bias = None


   def activate(self, x):
       return np.where(x >=  0, 1,0)

   def fit(self, x, y):
       samples, feautures = x.shape

       self.weights = np.zeros(feautures)
       self.bias = 0

       for i in range(self.n_iterations):
           output = np.dot(x, self.weights) + self.bias

           predict = self.activate(output)
           update = self.rate *(y-predict)

           self.weights += x.T @ update

   def predict(self, x):
       output = x @  self.weights + self.bias
       predicted  = self.activate(output)
       return predicted


x = np.array([[0,1] , [1,1], [0,0]])

y= np.array([1,1,0])

perceptron = Perceptron(rate=0.1, n_iterations=10)

perceptron.fit(x, y)

predicted =  perceptron.predict(np.array([[1,1]]))

print(predicted)


