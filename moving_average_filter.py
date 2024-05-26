import collections
import numpy as np
import matplotlib.pyplot as plt

class moving_average_filter():

    def __init__(self, n, dim):
        self.n = n
        self.buffer = collections.deque(np.array([]))
        self.sum = np.zeros(dim)
        self.average = np.zeros(dim)

    def add_sample(self, sample):
        self.buffer.append(sample)
        self.sum += sample
        while len(self.buffer) > self.n:
            self.sum -= self.buffer[0]
            self.buffer.popleft()
        avg_float = self.sum/len(self.buffer)
        self.average = avg_float.astype(np.uint8)

if __name__=="__main__":

    filt = moving_average_filter(100, 2)
    t_array = np.arange(0,10,1/200)
    filter_log = np.array([]).reshape((-1,2))
    signal_log = np.array([]).reshape((-1,2))
    for t in t_array:

        signal = np.array([np.sin(t), np.cos(t)]) + np.random.normal(size=2)
        filt.add_sample(signal)
        filter_log = np.vstack((filter_log, filt.average))
        signal_log = np.vstack((signal_log, signal))

    plt.subplot(2,1,1)
    plt.plot(t_array, signal_log[:,0], '--')
    plt.plot(t_array, filter_log[:,0])
    plt.legend(['original signal', 'filtered signal'])
    plt.ylabel('signal 0')
    plt.xlabel('t')
    plt.subplot(2,1,2)
    plt.plot(t_array, signal_log[:,1], '--')
    plt.plot(t_array, filter_log[:,1])
    plt.legend(['original signal', 'filtered signal'])
    plt.ylabel('signal 1')
    plt.xlabel('t')
    plt.show()