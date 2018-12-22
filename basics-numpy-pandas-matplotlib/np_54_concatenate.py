
import numpy as np
a = np.array([[1,2,3],[4,4,4],[5,6,7]])
b = np.array([[0,0,0],[8,8,8],[9,9,9]])
print(a)
print(b)

c = np.concatenate((a,b))
print(c)