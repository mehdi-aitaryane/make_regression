# Make_Regression

This project generates and visualizes regression datasets with two modules: datasets.py and plots.py. The datasets.py module creates feature and target arrays with a random linear model, noise, and a low rank-fat tail singular profile. The plots.py module shows the regression line with 2D or 3D plots. The project also has an example notebook that uses the modules.

## Mathematics Behind the Algorithm
The algorithm is based on the concept of linear regression. The goal is to find a linear function that best fits the data points. The algorithm initializes weights and bias randomly, generates random features and adds noise, calculates predicted values using the equation of a linear function, and adjusts the features to satisfy the equation.

## Pseudocode of the Algorithm
The pseudocode describes the steps of the make_regression function, which takes the number of samples, features, noise, random state, and initialization function as input, and returns the feature and target arrays as output.

```
Procedure make_regression:
  Input: n_samples, n_features, noise, random_state, init:
  set the random seed to random_state
  create weights and bias using init function
  create features using uniform random distribution
  add noise to features using normal random distribution
  create targets using linear function of features, weights, and bias
  return features and targets
```

## Modules
The project contains two modules: datasets.py and plots.py. The datasets.py module has functions to generate and print the regression dataset. The plots.py module has functions to create 2D or 3D plots of the dataset.

## Notebook
The project has an example notebook that demonstrates how to use the modules to generate and visualize a regression dataset. The notebook imports the modules, generates a dataset using the make_regression function, and visualizes the dataset using the plot2D or plot3D functions.

## Usage
To use the project, you need to import the modules, generate a dataset using the make_regression function, and visualize the dataset using the plot2D or plot3D functions.

## Contributing
The project welcomes contributions from other users. They can open an issue or submit a pull request with their ideas or changes.

## License
The project is licensed under the terms of the MIT license.

