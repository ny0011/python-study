import sys
import os
sys.path.append(f"{os.environ['HOME']}/python-study/300/")
print(sys.path)

# or using PYTHONPATH
# ex) $ PYTHONPATH="${HOME}/python-study/300/" python

from quest import Quest

PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def add(a,b):
    return a+b

a= Quest(1,5)
print(a)




