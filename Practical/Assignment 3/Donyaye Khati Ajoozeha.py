import numpy as np
from math import inf

class LPSolver(object):
    EPS = 1e-9
    NEG_INF = -inf

    def __init__(self, A, b, c):
        self.m = len(b)
        self.n = len(c)
        self.N = [0] * (self.n + 1)
        self.B = [0] * self.m
        self.D = [[0 for i in range(self.n + 2)] for j in range(self.m + 2)]
        self.D = np.array(self.D, dtype=np.float64)
        for i in range(self.m):
            for j in range(self.n):
                self.D[i][j] = A[i][j]
        for i in range(self.m):
            self.B[i] = self.n + i
            self.D[i][self.n] = -1
            self.D[i][self.n + 1] = b[i]
        for j in range(self.n):
            self.N[j] = j
            self.D[self.m][j] = -c[j]
        self.N[self.n] = -1
        self.D[self.m + 1][self.n] = 1

    def Pivot(self, r, s):
        D = self.D
        B = self.B
        N = self.N
        inv = 1.0 / D[r][s]
        dec_mat = np.matmul(D[:, s:s + 1], D[r:r + 1, :]) * inv
        dec_mat[r, :] = 0
        dec_mat[:, s] = 0
        self.D -= dec_mat
        self.D[r, :s] *= inv
        self.D[r, s + 1:] *= inv
        self.D[:r, s] *= -inv
        self.D[r + 1:, s] *= -inv
        self.D[r][s] = inv
        B[r], N[s] = N[s], B[r]

    def Simplex(self, phase):
        m = self.m
        n = self.n
        D = self.D
        B = self.B
        N = self.N
        x = m + 1 if phase == 1 else m
        while True:
            s = -1
            for j in range(n + 1):
                if phase == 2 and N[j] == -1:
                    continue
                if s == -1 or D[x][j] < D[x][s] or D[x][j] == D[x][s] and N[j] < N[s]:
                    s = j
            if D[x][s] > -self.EPS:
                return True
            r = -1
            for i in range(m):
                if D[i][s] < self.EPS:
                    continue
                if r == -1 or D[i][n + 1] / D[i][s] < D[r][n + 1] / D[r][s] or (D[i][n + 1] / D[i][s]) == (
                        D[r][n + 1] / D[r][s]) and B[i] < B[r]:
                    r = i
            if r == -1:
                return False
            self.Pivot(r, s)

    def Solve(self):
        m = self.m
        n = self.n
        D = self.D
        B = self.B
        N = self.N
        r = 0
        for i in range(1, m):
            if D[i][n + 1] < D[r][n + 1]:
                r = i
        if D[r][n + 1] < -self.EPS:
            self.Pivot(r, n)
            if not self.Simplex(1) or D[m + 1][n + 1] < -self.EPS:
                return self.NEG_INF, None
            for i in range(m):
                if B[i] == -1:
                    s = -1
                    for j in range(n + 1):
                        if s == -1 or D[i][j] < D[i][s] or D[i][j] == D[i][s] and N[j] < N[s]:
                            s = j
                    self.Pivot(i, s)
        if not self.Simplex(2):
            return self.NEG_INF, None
        x = [0] * self.n
        for i in range(m):
            if B[i] < n:
                x[B[i]] = D[i][n + 1]
        return D[m][n + 1], x

m, N, H = list(map(int, input().split()))
A = [[-1], [-1]]
A[0].clear()
A[1].clear()
B = []
B.append(-N)
B.append(-H)
C = []
C = [-1 for i in range(m)]
for i in range(m):
    first, second = list(map(int, input().split()))
    A[0].append(-first)
    A[1].append(-second)
result = LPSolver(A, B, C)
output = -result.Solve()[0]
print(output)