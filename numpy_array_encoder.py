import json
from json import JSONEncoder
import numpy

# https://pynative.com/python-serialize-numpy-ndarray-into-json/
class numpy_array_encoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
