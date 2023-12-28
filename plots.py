import matplotlib.pyplot as plt

def plot2D(title, xlabel, ylabel, X, y):
    plt.plot(X[:, 0], y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

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