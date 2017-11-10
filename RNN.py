import tensorflow as tf
from tensorflow.contrib import rnn

learning_rate = 0.01
epoch = 10000
batch_size =
diplay_size = 200


#Network params
n_inputs = 24
timesteps = 24
n_hidden = 1000
n_classes = 576


X = tf.placeholder("float", [None, timesteps, n_inputs])
Y = tf.placeholder("float", [None, n_classes])

weights = {
    'out' : tf.Variable(tf.random_normal([n_hidden, n_classes]))
}

biases = {
    'out' : tf.Variable(tf.random_normal([n_classes]))
}

def RNN(x, w, b):
    x = tf.unstack(x, timesteps, -1)
    lstm = rnn.BasicLSTMCell(n_hidden, forget_bias=1.0)

    y, states = rnn.static_rnn(lstm, x, dtype=tf.float32)
    return tf.matmul(y[-1], weights['out']) + biases['out']


logits = RNN(X, weights, biases)

predict = tf.nn.softmax(logits)

#define loss and optimizer
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)


#Actual prediction
actual_pred = tf.equal(tf.argmax(predict, 1), tf.argmax(Y, 1))
accu = tf.reduce_mean(tf.cast(actual_pred, tf.float32))

init = tf.global_variables_initializer()

with tf.Session as sess:
    sess.run(init)

    for step in range(1, epoch+1):
        batch_x, batch_y = mn

        batch_x.reshape((batch_size, timesteps, n_inputs))
        sess.run(train_op, feed_dict={X: batch_x, Y: batch_y})
        if step == 1 or step%diplay_size==0:
            loss, acc = sess.run([loss_op, accuracy], feed_dict={X: batch_x,
                                                                 Y: batch_y})
            print("Step " + str(step) + ", Minibatch Loss= " +"{:.4f}".format(loss) + ", Training Accuracy= " +"{:.3f}".format(acc))

    print("Optimization Finished!")

    # Calculate accuracy for 128 mnist test images
    test_len = 128
    test_data = mnist.test.images[:test_len].reshape((-1, timesteps, n_inputs))
    test_label = mnist.test.labels[:test_len]
    print("Testing Accuracy:", sess.run(accu, feed_dict={X: test_data, Y: test_label}))
