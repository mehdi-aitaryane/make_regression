import numpy as np

# Random Initialization
def random_init(size_in, size_out):
    return np.random.uniform(0.0, 1.0, size=(size_in, size_out))

def print_shape(X, y):
    print("X shape is ", X.shape)
    print("y shape is ", y.shape)

def sort_dataset(X, y):
    idx = np.argsort(y)
    return X[idx], y[idx]

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
