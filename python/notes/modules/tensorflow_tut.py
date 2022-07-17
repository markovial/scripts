import tensorflow as tf
import numpy as np
# Tensors are vasically the same as
# - np.array     : multi-dim arrays in numpy
# - pd.dataframe : dataframes in pandas

print(tf.__version__)

# intialize
# tf.zeros()
# tf.ones()

X = tf.constant(np.random.randn(3,1), name = "X")
W = tf.constant(np.random.randn(4,3), name = "W")
b = tf.constant(np.random.randn(4,1), name = "b")
res =tf.add( W , b ) # Matrix add
res = tf.matmul( W , X ) # Matrix multiply

res = W @ X # Matrix multiply shortform
res = W + b # matrix add shortform



# z = tf.cast(z, tf.float32)
# a = tf.keras.activations.sigmoid(z)

# tf.one_hot(labels, depth, axis=0) # one hot enconding
# tf.reshape( matrix , shape )      # reshape matrix

# tf.reshape( X , (length , 1) ) # vector of shape = (length , 1)
# tf.reshape( X , (length ,  ) ) # idk the difference , but it is different
# tf.reshape( X , length )       # vector of shape = (length ,  )
# tf.reshape( X , -1 )           # vector of shape = (length , )

# tf.sigmoid
# tf.softmax

