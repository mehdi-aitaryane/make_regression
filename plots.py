import matplotlib.pyplot as plt

# This function plots a 2D line graph of X and y
# title: the title of the graph
# xlabel: the label of the x-axis
# ylabel: the label of the y-axis
# X: a 2D array of features
# y: a 1D array of targets

def plot2D(title, xlabel, ylabel, X, y):
    plt.plot(X[:, 0], y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# This function plots a 3D surface graph of X and y
# title: the title of the graph
# xlabel: the label of the x-axis
# ylabel: the label of the y-axis
# zlabel: the label of the z-axis
# X: a 2D array of features
# y: a 1D array of targets

def plot3D(title, xlabel, ylabel, zlabel, X, y):
    # Creating plot
    ax = plt.axes(projection ="3d")
    ax.plot3D(X[:, 0], X[:, 1], y)
    plt.title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    # Rotate the plot (change the angles as needed)
    ax.view_init(elev=30 , azim=-80 )
    plt.show()