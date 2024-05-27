import collections
import numpy as np

class delta_frames():

    def __init__(self):
        self.buffer = collections.deque(np.array([]))

    def add_frame(self, frame):
        self.buffer.append(frame)

    def dump_frames(self):
        delta_frame_dump = collections.deque(np.array([]))
        for i, d_frame in enumerate(self.buffer):
            if i > 0:
                delta_frame_dump.append(d_frame - self.buffer[i - 1])
        return list(delta_frame_dump)
