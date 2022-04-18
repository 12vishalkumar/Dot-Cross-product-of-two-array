import numpy as np
n = int(input())
A = np.array([list(map(int, input().split())) for i in range(n)])
B = np.array([list(map(int, input().split())) for i in range(n)])
print(np.dot(A, B))



