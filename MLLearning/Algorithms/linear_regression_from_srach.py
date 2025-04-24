import numpy as np

class LinearRegression:
    """
        A simple implementation of Linear Regression using gradient descent.
    """
    def __init__(self,learning_rate, n_iterations):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
    
    def fit(self, X, y):
        """
            Fit the model to the training data.
        """
        self.m, self.n = X.shape
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.y = y

        # implementing Gradient Descent for Optimization
                  
        for i in range( self.no_of_iterations ) :
            self.update_weights()
        
    # function to update weights in gradient descent
      
    def update_weights( self ) :
        Y_prediction = self.predict( self.X )

        # calculate gradients  
        dw = - ( 2 * ( self.X.T ).dot( self.y - Y_prediction )  ) / self.m
        db = - 2 * np.sum( self.y - Y_prediction ) / self.m 
          
        # updating the weights
        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db
          
      
    # Line function for prediction:
      
    def predict( self, X ) :
        return X.dot( self.w ) + self.b