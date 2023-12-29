import numpy as np

# This function returns a random array of the given shape
# size_in: the number of rows of the array
# size_out: the number of columns of the array

def random_init(size_in, size_out):
    return np.random.uniform(0.0, 1.0, size=(size_in, size_out))

# This function prints the shape of the feature and target arrays
# X: a 2D array of features
# y: a 1D array of targets

def print_shape(X, y):
    print("X shape is ", X.shape)
    print("y shape is ", y.shape)

# This function sorts the feature and target arrays by the target values
# X: a 2D array of features
# y: a 1D array of targets

def sort_dataset(X, y):
    idx = np.argsort(y)
    return X[idx], y[idx]

# This function generates a regression dataset based on a random linear model
# n_samples: the number of samples in the dataset
# n_features: the number of features in the dataset
# noise: the standard deviation of the noise added to the features
# random_state: the seed for the random number generator
# init: the function to initialize the weights and bias of the linear model

def make_regression(n_samples=101, n_features=20, noise = 0.0, random_state=None, init = random_init):
    np.random.seed(random_state)

    # Initialize weights and bias
    weights = init(1, n_features)[0]
    bias = init(1, 1)[0]

    # Generate random features
    X = np.random.uniform(size = (n_samples, n_features))

    # Add noise to features before any adjustments
    X += np.random.normal(scale=noise, size=(n_samples, n_features))

    # Calculate y_pred such that X * weights + bias = y
    y = np.dot(X, weights) + bias

    return X, y
