"""
    A convolutional network implementation example using TensorFlow library
"""

import tensorflow as tf

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('tensorflow_execise/MNIST_data/',one_hot=True)

# Parameters
learning_rate = 0.001
training_iters = 200000
batch_size = 128
display_step = 10

# Network Paramerters
n_input = 784 # MNIST data input(img shape:28*28)
n_classes = 10 # MNIST total classes(0-9 digits)
dropout = 0.75
