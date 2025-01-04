# -*- coding: utf-8 -*-
"""linear_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zTLmZOh3mP0gNwSClOhSsz1aZCiybQds
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a=pd.read_csv('/content/linear_regression_train.csv')

x_train=a.values[0:48000,1:26]
y_train=a.values[0:48000,26:27]

def cost_function(x,y,w,b):
  m=x.shape[0]
  f_wb=np.matmul(x,w)+b
  cost=np.sum(f_wb-y)**2
  cost=cost/(2*m)
  return cost
def compute_gradient(x,y,w,b):
  m,n=x.shape
  dj_dw=np.zeros((n,1))
  dj_db=0
  f_wb=np.matmul(x,w)+b
  dj_dw=np.matmul(x.T,(f_wb-y))
  dj_db= np.sum(f_wb-y)
  dj_db=dj_db/m
  dj_dw=(dj_dw)/m
  return dj_dw,dj_db

def gradient_descent(x,y,w,b,alpha,iterations):
  m,n=x.shape
  J_history=[]
  for i in range(iterations):
    dj_dw,dj_db=compute_gradient(x,y,w,b)
    w=w-alpha*dj_dw
    b=b-alpha*dj_db

    if i<=iterations:
      J_history.append(cost_function(x,y,w,b))

    if i%1000==0:
            print(f"Iteration {i:4d}: Cost {J_history[-1]}   ")
  return w,b,J_history

w=np.zeros((25,1))
b=0
alpha=0.000025
iterations=10000
w,b,J_history=gradient_descent(x_train,y_train,w,b,alpha,iterations)
print(f'w={w}')
print(f'b={b}')

w=[[ 14.3101927 ],
 [  7.12840192],
 [ 12.28139942],
 [ 18.30065748],
 [ -1.55466007],
 [ 47.46819523],
 [ 12.01915638],
 [ -7.4460637 ],
 [ 15.39091356],
 [  7.08996842],
 [ -0.19923018],
 [ -0.45221417],
 [ 23.86069166],
 [ 58.8402542 ],
 [  1.59787588],
 [ 26.35200169],
 [  0.42111356],
 [ 13.52967051],
 [ 30.78512158],
 [ 44.36070349],
 [  1.97275345],
 [ -0.29731694],
 [-27.19693617],
 [ 12.07977455],
 [  0.12715325]]

b=2.936144949410182

test=pd.read_csv('/content/linear_regression_test.csv')
x_test=test.values[0:12000,1:26]

y_predicted=np.matmul(x_test,w)+b
print(f'y_predicted={y_predicted}')
cost=cost_function(x_test,y_predicted,w,b)
print(f'cost={cost}')

