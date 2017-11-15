import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn

learning_rate = 0.01
epoch = 10000
batch_size = 1
diplay_size = 200

# Network params
n_inputs = 22
timesteps = 22
n_hidden = 700
n_classes = 484

X = tf.placeholder("float", [None, timesteps, n_inputs])
Y = tf.placeholder("float", [None, n_classes])

weights = {
    'out': tf.Variable(tf.random_normal([n_hidden, n_classes]))
}

biases = {
    'out': tf.Variable(tf.random_normal([n_classes]))
}

def RNN(x, w, b):
    x = tf.unstack(x, timesteps, -1)
    lstm = rnn.BasicLSTMCell(n_hidden, forget_bias=1.0)

    y, states = rnn.static_rnn(lstm, x, dtype=tf.float32)
    return tf.matmul(y[-1], weights['out']) + biases['out']


def splitData(data):
    for i in range(len(data)):
        if data[i] == 1:
            return data, i

def getPrediction(training, testing):
    #tf.reset_default_graph()
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

    ind = 0

    with tf.Session() as sess:
        sess.run(init)

        for step in range(1, epoch+1):
            tbatch_x, tbatch_y = splitData(training[ind])
            batch_x = batch_y = []
            batch_x.append(np.asarray(tbatch_x))
            batch_y.append(np.asarray(tbatch_y))
            batch_x = np.asarray(batch_x)
            batch_y = np.asarray(batch_y)
            ind += 1
            batch_x.reshape((batch_size, timesteps, n_inputs))
            sess.run(train_op, feed_dict={X: batch_x, Y: batch_y})
            if step == 1 or step%diplay_size == 0:
                loss, acc = sess.run([loss_op, accu], feed_dict={X: batch_x,
                                                                     Y: batch_y})
                print("Step " + str(step) + ", Minibatch Loss= " +"{:.4f}".format(loss) + ", Training Accuracy= " +"{:.3f}".format(acc))

        print("Optimization Finished!")

        # Calculate accuracy for 128 mnist test images
        test_data, test_label = splitData(testing)
        test_data = np.asarray(test_data)
        test_label = np.asarray(test_label)

        test_data = test_data.reshape((-1, timesteps, n_inputs))

        # test_data = mnist.test.images[:test_len].reshape((-1, timesteps, n_inputs))
        # test_label = mnist.test.labels[:test_len]
        print("Testing Accuracy:", sess.run(accu, feed_dict={X: test_data, Y: test_label}))


def getBinaryString(time):
    time = int(time)
    temp = np.zeros(484)
    temp[time] = 1
    return temp

trainData = [line.rstrip('\n') for line in open('TestData/trainData.txt')]
testData = [line.rstrip('\n') for line in open('TestData/testData.txt')]
trainDict = {}
testDict = {}

for i in trainData:
    item = i.split('\t')
    if item[0] in trainDict.keys():
        trainDict[item[0]].append(getBinaryString(item[3]))
    else:
        tempList = []
        tempList.append(getBinaryString(item[3]))
        trainDict[item[0]] = tempList

for i in testData:
    item = i.split('\t')
    testDict[item[0]] = getBinaryString(item[3])

for user in trainDict.keys():
    print ("For user:"+user)
    getPrediction(trainDict[user], testDict[user])

