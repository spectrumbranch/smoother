import json
from numpy_array_encoder import numpy_array_encoder

class file_io():

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, data):
        with open(self.file_name, "w") as outfile:
            outfile.write(json.dumps(data, cls=numpy_array_encoder))
        print("Written object", data)

    def read(self):
#         with open(self.file_name, "r") as infile:
#             data = pickle.load(infile)
        print("Reconstructed object", data)
        return data
