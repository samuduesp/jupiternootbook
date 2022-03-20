## jupiternootbook

This is example help you to undertsand the basic Data analysis using python 

## intallation 

#### JupyterLab

Install JupyterLab with pip:
```
pip install jupyterlab
```
Note: If you install JupyterLab with conda or mamba, we recommend using the conda-forge channel.

Once installed, launch JupyterLab with:
```
jupyter-lab
Jupyter Notebook
```
#### Install the classic Jupyter Notebook with:
```
pip install notebook
```
To run the notebook:
```jupyter notebook
```
#### Voilà
Install Voilà with:
```
pip install voila
```

#### other required modules
```
pip install lxml
pip install matplotlib
```
Note - if you see any module error we need add that module to run the examples
### Linear Regression in Python

Linear Regression is a machine learning algorithm based on supervised learning. Linear Regression is a predictive model that is used for finding the linear relationship between a dependent variable and one or more independent variables. Here,dependent variable/target variable(Y) should be continuous variable.


#### R²( R square )→ Coefficient of determination

The coefficient of determination → This metric is used after building the model, to check how reliable the model is.
R² →It is equal to the variance explained by regression (Regression Error or SSR) divided by Total variance in y (SST)
R² → It describes how much of the total variance in y is explained by our model.
If Error(unexplained error or SSE)<Variance (SST) means the model is good.
The best fit is the line in which unexplained error (SSE) is minimized.
R² values range from 0 to 1.
0 → indicates Poor model
1 or close to 1 → indicates the Best model