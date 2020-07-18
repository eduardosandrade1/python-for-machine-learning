import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([(1,2,3),(4,5,6),[7,8,9]])
print(b)

#matriz com varios zeros
c = np.zeros((10,10))
print(c)

#matrix com ums
d = np.ones((10,10))
print(d)

#na diagonal aparecem ums N por N
e = np.eye(5)
print(e)

#maior elemento
print(b.max())
#menor elemento
print(b.min())

#soma total da matriz
print(b.sum())

#media da matriz
print(b.mean())