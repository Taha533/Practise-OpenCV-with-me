from math import sqrt
from pprint import pprint

def cholesky(A):
    L = [[0.0] * len(A) for _ in range(len(A))]
    for i, (Ai, Li) in enumerate(zip(A, L)):
        for j, Lj in enumerate(L[:i+1]):
            s = sum(Li[k] * Lj[k] for k in range(j))
            Li[j] = sqrt(Ai[i] - s) if (i == j) else \
                      (1.0 / Lj[j] * (Ai[j] - s))
    return L

m1 = [[25, 15, -5],
     [15, 18,  0],
     [-5,  0, 11]]
a = cholesky(m1)
import numpy as np
#a = a.reshape(3,3)
#print("Lower Triangular:\n{}".format(a))
print("Lower Triangular:\n{}".format(cholesky(m1)))

m2 = [[18, 22,  54,  42],
          [22, 70,  86,  62],
          [54, 86, 174, 134],
          [42, 62, 134, 106]]
print("Lower Triangular:\n{}".format(cholesky(m2)))