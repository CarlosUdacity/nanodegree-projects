# Simple Neural Network

This project implements a simple **single-layer feed-forward network**, or **single-layer perceptron** using only **NumPy** as dependency.

![single_layer_perceptron](https://user-images.githubusercontent.com/19690196/29979427-c76ebff8-8f1b-11e7-9f1a-1f1a796a8e90.png)

We trained our neural network using 4 samples with 3 features:
<img src="http://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;0&space;&&space;0&space;&&space;1\\&space;1&space;&&space;1&space;&&space;1\\&space;1&space;&&space;0&space;&&space;1\\&space;0&space;&&space;1&space;&&space;1&space;\end{bmatrix}" title="\begin{bmatrix} 0 & 0 & 1\\ 1 & 1 & 1\\ 1 & 0 & 1\\ 0 & 1 & 1 \end{bmatrix}" />
<br/>
and considered the following output:
<br/>
<img src="http://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;0\\&space;1\\&space;1\\&space;0&space;\end{bmatrix}" title="\begin{bmatrix} 0\\ 1\\ 1\\ 0 \end{bmatrix}" />

We used the **Sigmoid function** as step function, and trained the network to predict the output for the new element:

<img src="http://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0&space;\end{bmatrix}" title="\begin{bmatrix} 1 & 0 & 0 \end{bmatrix}" />

<br/>
For more information, please refer to 

[Deep Learning Nanodegree](https://classroom.udacity.com/nanodegrees/nd101/parts/808fb7e7-aa95-4ed2-9040-8cabb07dd232/modules/329a736b-1700-43d4-9bf0-753cc461bebc/lessons/c3dd053a-7660-4fc5-8bdc-53301ac7ce51/concepts/9f6f9683-3f44-43a3-9d5b-f30fad2b6127)