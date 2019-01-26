# from https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/
# A DP is an algorithmic technique which is usually based on a recurrent formula and one (or some) starting states
# A sub-solution of the problem is constructed from previously found ones. 
# faster running time than other techniques like backtracking, brute-force etc.

# 1. sub-problem: #how to find states #sub-functions
## sum i, index k 
## maximum cost, position
## with j money being left

# Introduction (Beginner)
# Find the minimum number of coins the sum of which is S
def min_coins_sum(y, s):
    V = [1, 3, 5]
    s = 11
    Nmin = np.ones(s + 1) * np.inf
    Nmin[0] = 0
    for i in range(1, s + 1):
        for j in range(len(V)):
            if V[j] <= i and Nmin[i - V[j]] + 1 < Nmin[i]:
                Nmin[i] = Nmin[i - V[j]] + 1
    return Nmin[s]


# Elementary - recurrent relation
# Find the length of the longest non-decreasing sequence.
def longest_seq(A):
    A = [5, 3, 4, 8, 6, 7]
    rst = [1]*len(A)
    for i in range(1, len(A)):
        if A[i]<=A[i-1]:
            rst[i] = rst[i-1]+1
    return max(rst)


# Intermediate - bi-dimensional DP problems
# Find the maximum number of apples you can collect
def max_grid_apples(A):
    A = np.random.randint(10, dtype=int, size=(3,3))
    n = A.shape[0]
    m = A.shape[1]
    rst = np.zeros((n+1, m+1))
    for i in range(n):
        for j in range(m):
            rst[i][j] = A[i][j] + max(rst[i][j-1], rst[i-1][j])
    return rst[n-1][m-1]


# Upper-Intermediate -  dealing DP
# Find the shortest path from vertex 1 to vertex N
def min_path(E, Dist, M, t):
    MinM = np.ones((n, M)) * np.inf
    for (p,k) in E[k]:
        if MinM[p][l - S[p]] > MinM[k][l] + Dist[k][p]):
            MinM[p][l - S[p]] = MinM[k][l] + Dist[k][p]
    return MinM[t][M]


# Advanced
# Find the maximum number of apples you can collect
def max_grid_apples(M):
    M = np.random.randint(10, size=(6, 6))
    M = ["0123456789",
         "1123456789",
         "2223456789",
         "3333456789",
         "4444456789",
         "5555556789",
         "6666666789",
         "7777777789",
         "8888888889",
         "9999999999"]
    def midway(y, ip, i):
        res = 0
        for x in range(ip, i + 1):
            res += int(M[y][x])
        return res

    def findbest(y, i, j, k, best):
        cur = 0
        for ip in range(0, i + 1):
            for jp in range(i + 1, j + 1):
                for kp in range(j + 1, k + 1):
                    cur = max(cur, best[ip][jp][kp] + midway(y, ip, i) + midway(y, jp, j) + midway(y, kp, k))
        return cur

    m = len(M)
    n = 10
    best = np.zeros((n,n,n))

    for y in range(m):
        cur = np.zeros((n, n, n))
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    cur[i][j][k] = findbest(y, i, j, k, best)
        best = cur
    return best[m - 3][m - 2][m - 1]
