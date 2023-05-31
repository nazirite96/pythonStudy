import numpy as np
import torch
t = np.array([0., 1., 2., 3., 4., 5., 6.])

print(t)

print('Rank of t: ', t.ndim)
print('Shape of t: ', t.shape)

print('t[0] t[1] t[-1] = ', t[0], t[1], t[-1])


print('t[2:5] t[4:-1]  = ', t[2:5], t[4:-1])

print('t[:2] t[3:]     = ', t[:2], t[3:])


t = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [10., 11., 12.]])
print(t)

print('Rank  of t: ', t.ndim)
print('Shape of t: ', t.shape)

t = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6.])
print(t)

print(t.dim())  # rank. 즉, 차원
print(t.shape)  # shape
print(t.size()) # shape

print(t[0], t[1], t[-1])  # 인덱스로 접근
print(t[2:5], t[4:-1])    # 슬라이싱
print(t[:2], t[3:])       # 슬라이싱


t = torch.FloatTensor([[1., 2., 3.],
                       [4., 5., 6.],
                       [7., 8., 9.],
                       [10., 11., 12.]
                       ])
print(t)

print(t.dim())  # rank. 즉, 차원
print(t.size()) # shape

print(t[:, 1]) # 첫번째 차원을 전체 선택한 상황에서 두번째 차원의 첫번째 것만 가져온다.
print(t[:, 1].size()) # ↑ 위의 경우의 크기

print(t[:, :-1])


m1 = torch.FloatTensor([[3, 3]])
m2 = torch.FloatTensor([[2, 2]])
print(m1 + m2)

# Vector + scalar
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([3]) # [3] -> [3, 3]
print(m1 + m2)

# 2 x 1 Vector + 1 x 2 Vector
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([[3], [4]])
print(m1 + m2)

m1 = torch.FloatTensor([[1, 2], [3, 4]])
m2 = torch.FloatTensor([[1], [2]])
print('Shape of Matrix 1: ', m1.shape) # 2 x 2
print('Shape of Matrix 2: ', m2.shape) # 2 x 1
print(m1.matmul(m2)) # 2 x 1

m1 = torch.FloatTensor([[1, 2], [3, 4]])
m2 = torch.FloatTensor([[1], [2]])
print('Shape of Matrix 1: ', m1.shape) # 2 x 2
print('Shape of Matrix 2: ', m2.shape) # 2 x 1
print(m1 * m2) # 2 x 2
print(m1.mul(m2))

t = torch.FloatTensor([1, 2])
print(t.mean())
t = torch.FloatTensor([[1, 2], [3, 4]])
print(t)

print(t.mean())

print(t.mean(dim=0))


print(t.mean(dim=1))

t = torch.FloatTensor([[1, 2], [3, 4]])
print(t)
t = torch.FloatTensor([[1, 2], [3, 4]])