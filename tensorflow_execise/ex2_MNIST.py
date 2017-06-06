# coding:utf-8

# Just like programming has Hello World, machine learing has MNIST.

# The MNIST database (Modified National Institute of Standards and Technology
# database) is a large database of handwritten digits that is commonly used for
# training various image processing systems.
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("tensorflow_execise/MNIST_data/",one_hot=True)
# The MNIST data is split into three parts: 55000 data points of training data
# (mnist.train), 10000 points of test data(mnist.test), and 5000 points of
# validation data(mnist.validation). This split is very important:it's essential
# in machine learning that we have separate data which we don't learn from so
# that we can make sure that we've learned actually generalizes!

# x isn't a specific value. It's a placeholder, a value that we'll input when
# we ask tensorflow to run a computation. We want to be able to input any
# number of MNIST images, each flattened into a 784-dimensional vector. We
# represent this a 2-D tensor of floating-point numbers, with a shape [None,784]print 6299/12
# None means that a dimension can be of any length.
x = tf.placeholder(tf.float32,shape=[None,784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
# implement our model
y = tf.nn.softmax(tf.matmul(x,W) + b)
# To implement cross-entropy we need to first add a new placeholder to input the
# correct answers
y_ = tf.placeholder(tf.float32,shape=(None,10))
# The we can implement the cross-entropy function -Ey_log(y):
# The tf.reduce_sum adds the elements in the second dimension of y, due to the
# reduction_indices=[1]
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y),reduction_indices=[1]))
# Now that we know what we want our model to do,it's very easy to have tensorflow
# train it to do so. Because TensorFlow knows the entire graph of your computations
# it can automatically use the Backpropagation Algorithm to efficiently determine
# how your variables affect the loss you ask it to minimize.Then it can apply
# your choice of optimization algorithm to modify the variables and reduce the
# loss.
# 0.5 is the learning rate
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
# launch the model in an InteractiveSession:
sess = tf.InteractiveSession()
# initialize the variables we created:
tf.global_variables_initializer().run()
# begin train
for _ in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
# evaluate our model
# Well, first let's figure where we predicted the correct label. tf.argmax is an
# extremely useful function which gives you the index of the highest entry in a
# tensor along some axis. For example, tf.argmax(y,1) is the label our model
# thinks is most likely for each input, while tf.argmax(y_,1) is the correct
# label. We can use tf.equal to check if our prediction matches the truth.
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
# this gives us a list of booleans. To determine what fraction are corrrect, we
# cast to floating point numbers and then take the mean. For example,
# [True,False,True,True] would become [1,0,1,1] which would become 0.75
# tf.cast for convert the input data to fixed type
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print sess.run(accuracy,feed_dict={x:mnist.test.images,y_:mnist.test.labels})
