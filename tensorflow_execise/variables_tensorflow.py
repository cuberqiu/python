import tensorflow as tf

# create two variables
weights = tf.Variable(tf.random_normal([784,200],stddev=0.35),name="weights")
biases = tf.Variable(tf.zeros([200]),name="biases")

print weights
print biases

a = tf.Variable(1,name='a')
print a

# build a dataflow graph
c = tf.constant([[1,2,3,4],[3,4,5,6]])
d = tf.constant([[1,1,1],[0,1,1],[1,1,1],[0,0,1]])
print c,d
# multiply the matrics c*d
e = tf.matmul(c,d)
print e
# construct a Session to execute the graph
sess = tf.Session()
# Execute the graph and store the value that e represents in result
result = sess.run(e)
print result
result_c = sess.run(c)
print result_c

num_a = tf.constant(2)
print num_a
num_b = tf.constant(3)
print num_b
a = sess.run(num_a+num_b)
print a

matric_a = tf.constant(1,shape=[2,3])
print sess.run(matric_a)
print matric_a.shape

# Basic operations with variable as graph input
# The value returned by the constructor represents the output
# of the Variable op.
# tf Graph input
# placeholder(dtype,shape=none,name=none) : insert a place for a tensor that
# will be always fed. Its value must be fed using the feed_dict()
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
# define some operations
add = tf.add(a,b)
mul = tf.multiply(a,b)
# launch the default graph
with tf.Session() as sess:
    # Run every operation with variable input
    print "Adding with variables: %i" % sess.run(add,feed_dict={a:2,b:3})
    print "Multiplication with variables: %i" %sess.run(mul,feed_dict={a:2,b:3})
