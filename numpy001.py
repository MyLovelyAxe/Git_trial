import numpy as np
a = np.arange(12).reshape(3,4)
b = np.ones_like(a)
c = np.vstack((a,b))
d = np.hstack((a,b))
print(c)
print(d)
print(a)