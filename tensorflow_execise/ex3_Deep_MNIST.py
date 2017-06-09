# coding:utf-8

# We will learn the basic building blocks of a TensorFlow model while constructing
# a deep convolutional MNIST classifier.


import tensorflow as tf
# load MNIST data
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("tensorflow_execise/MNIST_data/",one_hot=True)
# Start a TensorFlow InteractiveSession
# TensorFlow relies on a highly efficient C++ backend(后端) to do its computation
# The connection to this backend is called a session. The common usage for
# TensorFlow programs is to first create a graph and then launch it in a session.
# Here we instead use the convenient InteractiveSession class, which makes
# TensorFlow moer flexible about how you structure your code. It allows you to
# interleave(交错) operations which build a computation graph with ones that run
# the graph. InteractiveSession, then you should build the entire conputation
# graph before starting a seesion and launching the graph.
sess = tf.InteractiveSession()

# Build a softmax regression model
# placeholders
# The input images x will consist of a 2d tensor floating point numbers. Here we
# assign shape of [None,784], where 784 is the dimensionality of a single flattened
# 28 by 28 pixel MNIST image, and None indicates that the first dimension,
# corresponding to the batch size, can be of any size. The target output classes
# y_ will also consist of a 2d tensor, where each row is a one-hot 10-dimensional
# vector indicating which digit class (zero through nine) the corresponding MNIST
# image belongs to.s
x = tf.placeholder(tf.float32,shape=[None,784])
y_ = tf.placeholder(tf.float32,shape=[None,10])
# variables
# W is a 784x10 matrix,because we have 784 input features and 10 outputs.
# b is a 10-dimensional vector, because we have 10 classes
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
# Before Variables can be used within a session, they must be initialized using
# that session.This step takes the initial values that have already been specified
# and assigns them to each Variable.This can be done for all Variables at once:
sess.run(tf.global_variables_initializer())

# Predicted class and loss function
y = tf.matmul(x,W) + b
# Note that tf.nn.softmax_cross_entropy_with_logits internally applies the softmax
# on the model's unnormalized model prediction and sums across all classes, and
# tf.reduce_mean takes the average over these sums.
cross_entropy = tf.reduce_mean(\
                    tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=y))

# Train model
# What TensorFlow actually did in the single line was to add operations to the
# computation graph. These operations included ones to compute gradients,
# compute parameter update steps, and apply update steps to the parameters.
# The returned operation train_step, when run, will apply the gradient descent
# updates to the parameters. Training the model can therefore be accomplished
# by repeatedly running train_step.
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
# We load 100 training examples in each training iteration. We then run the
# train_step operation, using feed_dict to replace the placeholder tensors x and
# y_ with the trianing examples. Note that you can replace any tensor in your
# computation graph using feed_dict -- it's not restricted to just placeholders.
for _ in range(1000):
    batch = mnist.train.next_batch(100)
    train_step.run(feed_dict={x:batch[0],y_:batch[1]})

# Evaluate the model
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print accuracy.eval(feed_dict={x:mnist.test.images,y_:mnist.test.labels})


# Build A Multilayer Convolutional Network
# Weight Initialization
# To create this model, we're going to need to create a lot of weights and biases.
# One should generally initialize weights with a small amount of noise for
# symmetry(对称) breaking, and to prevent 0 gradients. Since we're using ReLU
# neurons, it is also good practice to initialize them with a slightly positive
# initial bias to avoid "dead neurons". Instead of doing this repeatedly while
# we build the model, let's create two handly functions to do it for us:
def weight_variable(shape):
    initial = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1,shape=shape)
    return tf.Variable(initial)

# Convolution and Pooling
# TensorFlow also gives a lot of flexibility in convolution and pooling operations.
# How do we handle the boundaries? What is our stride size? In this example, We're
# always going to choose the vanilla(香草) version. Our convolutions uses a stride
# of one and are zero padded so that the output is the same size as the input.
# Our pooling is plain old max pooling over 2x2 blocks. To keep our code cleaner,
# let's also abstract those operations into functions.
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

# First Convolutional Layer
# We can now implement our first layer. It will consist of convolution, followed
# by max pooling. The convolution will compute 32 features for each 5x5 patch.
# Its weight tensor will have a shape of [5,5,1,32].The first two dimensions are
# the patch size, the next is the number of input channels, and the last is the
# number of output channels. We will also have a bias vector with a component for
# each output channel
W_conv1 = weight_variable([5,5,1,32])
