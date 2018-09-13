from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

print(mnist.train.imags.shape)

# python -m pip install --upgrade pip