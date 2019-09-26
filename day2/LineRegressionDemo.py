import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# 简单线性回归
def normalize(x):
    mean = np.mean(x)
    std = np.std(x)
    x = (x - mean) / std
    return x

tf.