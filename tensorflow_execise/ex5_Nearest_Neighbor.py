# A nearest neighbor learning algorithm example using TensorFlow library
# This example is using the MNIST database of handwrite digits
import numpy as np
import tensorflow as tf

# import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

# In this example , we limit mnist data
Xtr,Ytr = mnist.train.next_batch(6000) #5000 for training
Xte,Yte = mnist.test.next_batch(200) # 200 for testing

# tf Graph input
xtr = tf.placeholder("float",[None,784])
xte = tf.placeholder("float",[784])

# Nearext Neighbor calculation using L1 Distance
# Calculate L1 Distance
distance = tf.reduce_sum(tf.abs(tf.add(xtr,tf.negative(xte))),reduction_indices=1)
# Prediction: Get min distance index(Nearest neighbor)
pred = tf.arg_min(distance,0)

accuracy = 0.
# Initializing the variables
init = tf.global_variables_initializer()

# Launch the Graph
with tf.Session() as sess:
    sess.run(init)

    # loop over test data
    for i in range(len(Xte)):
        # Get nearest neighbor
        nn_index = sess.run(pred,feed_dict={xtr:Xtr,xte:Xte[i,:]})
        print "Test",i,"Prediction:",np.argmax(Ytr[nn_index]),\
            "True Class:",np.argmax(Yte[i])
        # Calculate accuracy
        if np.argmax(Ytr[nn_index]) == np.argmax(Yte[i]):
            accuracy += 1./len(Xte)
    print "Done!"
    print "Accuracy:",accuracy
