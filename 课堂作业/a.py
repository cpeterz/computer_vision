import numpy as np
import matplotlib.pyplot as plt

H = np.array([12,-3-3j, 1+1j, 0,0,0,0,0,0,0,0,0,0,0, 1-1j, -3+3j])

def create(H, r = 0.9):
    N = len(H)
    L = int(N/2)
    A = np.zeros(N)

    for n in range(N):
        theta = -2 * np.pi * n * r/N
        for k in range(L):
            A[n] += H[k] * np.cos(theta * k)
    return A

def plots(A):
    N = len(A)
    for n in range(N):
        plt.plot([n,n], [0, A[n]], 'r')
    plt.plot(range(N), A, 'r')
    plt.title('频率采样结构')
    plt.xlabel('n')
    plt.ylabel('波幅')
    plt.show()

A = create(H)
plots(A)