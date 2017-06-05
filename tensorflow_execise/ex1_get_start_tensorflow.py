# coding:utf-8
import tensorflow as tf
import numpy as np

# The central unit of data in TensorFlow is the Tensor.
# A Tensor consists of a set of primitive values shaped into an array of any
# number of dimensions.
# A Tensor's rank is its numbers of dimensions.
node1 = tf.constant(3.0,tf.float32)
node2 = tf.constant(4.0)  # also tf.float32 implicitly

# Notice that printing the nodes does not output the values 3.0 and 4.0 as you
# expect. Instead, they are nodes that, when evaluatedd, would produce 3.0 and
# 4.0, respectively. To actually evaluate the nodes, we must run the computational
# graph within a session. A session encapsulates(封装) the control and state of the
# TensorFlow runtime
print (node1,node2)

# The following code creates a Session object and then invokes its run method to
# run enough of the computional graph to evaluate node1 and node2. By running
# the computional graph in a session as follows:
sess = tf.Session()
print sess.run([node1,node2])

node3 = tf.add(node1,node2)
print "notes3: %r" %node3
print "sess.run(node3): %r" %sess.run(node3)

# The graph is not especially interesting because it always produces a constant
# result. A graph can be parameterized to accept external inputs, known as
# placeholders. A placeholder is a promise to provide a value later.
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
add_ab = a + b # + provides a shortcut for tf.add(a,b)
# We can evaluate this graph with multiple inputs by using the feed_dict parameter
# to specify Tensors that provide concrete values to these placeholders:
print sess.run(add_ab,feed_dict={a:3,b:4.5})
print sess.run(add_ab,feed_dict={a:[2,4],b:[5,9]})
add_triple = add_ab * 3
print sess.run(add_triple,feed_dict={a:3,b:4.5})

# In machin learning we will typically want a model that can take arbtrary inputs
# such as the one above. To make the model trainable, we need to be able to modify
# the graph to get new oututs with the same input. Variables allow us to add trainable
# parameters to a grap. They are constructed with a type and initial value:
W = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3],tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x + b

# Constants are initialized when you call tf.constant, and their value can never
# change. By constrast, Variables are not initialized when you can call tf.Variables
# To initialize all the Variables in a TensorFlow program, you must explicitly
# call a special operations as follows:
init = tf.global_variables_initializer()
sess.run(init)
print W,b
# It is important to realize init is a handle to the TensorFlow sub-graph that
# initializes all the global Variables. Until we call sess.run, the variables are
# uninitialized.
# Since x is a placeholder, we can evaluate linear_model for serveral values of
# x simultaneously as follows:
print sess.run(linear_model,feed_dict={x:[1,2,3,4]})

# A loss function measures how far the current model is from the provided data.
# We'll use a standard loss model for linear regression, which sums the squares
# of the deltas between the current model and provided data.
# linear_model-y creates a vector where each element is the corresponding examples
# error dalta. We call tf.square to square that error. The ,we sum all squared
# errors to create a single scalar that abstracts the error of all examples using
# tf.reduce_sum:
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model-y)
loss = tf.reduce_sum(squared_deltas)
print sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]})
# We can improve this manually by reassigning the values of W and b to the perfect
# values of -1 and 1. A variable is initialized to the value provided to tf.variable
# but can be changed using operations like tf.assign. For example, W=-1 and b=1
# are the optimal parameters for our model. We can change W and b accordingly:
fixW = tf.assign(W,[-1.])
fixb = tf.assign(b,[1.])
sess.run([fixW,fixb])
print sess.run(loss,feed_dict={x:[1,2,3,4],y:[0,-1,-2,-3]})


# We guesses the "perfect" values of W and b, but the whole point of machine
# learning is to find the correct model parameters automatically.

# TensorFlow provides optimizers that slowly change each variable according to
# the magnitude of the derivative of loss with respect to that variable. In
# general, computing symbolic derivatives manually is tedious and error-prone.
# Consequently, TensorFlow can automatically produce derivatives given only a
# description of the model using the function tf.gradients. For simplicity,
# optimizers typically do this for you. For example:
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
sess.run(init)
# train data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]
for i in range(1000):
    sess.run(train,feed_dict={x:x_train,y:y_train})
curr_w,curr_b,curr_loss = sess.run([W,b,loss],{x:x_train,y:y_train})
print "W:%s, b:%s, loss:%s" %(curr_w,curr_b,curr_loss)

# tf.contrib.learn
# tf.contrib.learn is a high-level TensorFlow lisbrary simplifies the machanics
# learning, including the following:
# - running training loops
# - running evaluation loops
# - managing data sets
# - managing feeding

# Declare list of features. We only have one real-valued feature. There are many
# other types of colums that are more complicated and useful
features = [tf.contrib.layers.real_valued_column("x",dimension=1)]
# An estimator is the front end to invoke training and evaluation. There are
# many predefined types like linear regression, logistic regression, linear
# classification, logistic classifiction, and neural network classifiers and
# regressions. The following code provides an estimator that does linear
# regression.
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)
# TensorFlow provides many helper methods to read and set up data sets.
# Here we use 'numpy_input_fn'. We have to tell the function how many batches
# of data we want and how big each batch should be.
x = np.array([1.0,2.,3.,4.])
y = np.array([0.,-1.,-2.,-3.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x},y,batch_size=4,\
                                            num_epochs=1000)
# We can invoke 1000 training steps by invoking the 'fit' method and passing
# the training data set.
estimator.fit(input_fn=input_fn,steps = 1000)
# Here we evaluate how well our model did. In a real example, we should want to
# use a separate validation and testing data set to avoid overfitting.
print estimator.evaluate(input_fn=input_fn)
