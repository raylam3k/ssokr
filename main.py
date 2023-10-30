"""A test main"""
import numpy as np   # how do I konw which pacakge is preloaded
import pandas as pd  # both works
# import icecream as ic   # do pip install icecream in terminal

for i in range(10):
    print(i)

for j in ('a', 'b', 'c'):
    print(j)

a = np.arange(20).reshape(5, 4)
b = np.arange(20)

c = pd.DataFrame()
print(c)

ar = np.array( [ [ 1,2,3], [4,5,6], [7,8,9]] )
row = np.array( [ 10,11,12])

ar = np.vstack( (ar, row ))

print (ar)