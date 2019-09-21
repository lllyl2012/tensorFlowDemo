import tensorflow as tf

DATA_FILE = '../boston.csv'
BATCH_SIZE = 10
NUM_FEATURES = 14


def data_generator(filename):
    f_queue = tf.train.string_input_producer(filename)
    # 跳过第一行
    reader = tf.TextLineReader()

    value = reader.read(f_queue)

    record_defaults = [[0.0] for _ in range(NUM_FEATURES)]
    data = tf.decode_csv(value, record_defaults=record_defaults)
    features = tf.stack(tf.gather_nd(data,[[5],[10],[12]]))
    label = data[-1]

    dequeuemin_after_dequeue = 10 * BATCH_SIZE

    capacity = 20 * BATCH_SIZE
    feature_batch, label_batch = tf.train.shuffle_batch(
        [features,label],batch_size=BATCH_SIZE,capacity=capacity,
        min_after_dequeue=min)
