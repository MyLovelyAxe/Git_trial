import numpy as np
import torch

def swap(a, b):
    a, b = b, a
    return a, b

a = 23
b = 43

print(a)
print(b)

print(torch.__version__)
print(np.__version__)