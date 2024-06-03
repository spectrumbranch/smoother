import collections
import numpy as np

class delta_frames():

    def __init__(self, dim):
        self.buffer = collections.deque(np.array([]))
        self.delta = np.zeros(dim)
        self.delta_frame_dump = collections.deque(np.array([]))

    def add_frame(self, frame):
        self.buffer.append(frame)

    def update_delta(self):
        buffer_len = len(self.buffer)
        if buffer_len > 2:
            self.delta = self.buffer[buffer_len - 1] - self.buffer[buffer_len - 2]
            print(self.delta)

    def dump_frames(self):
        self.delta_frame_dump = collections.deque(np.array([]))
        for i, d_frame in enumerate(self.buffer):
            if i > 0:
                self.delta_frame_dump.append(d_frame - self.buffer[i - 1])
        return list(self.delta_frame_dump)
