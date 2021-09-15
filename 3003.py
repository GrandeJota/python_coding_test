from sys import stdin
import math

chess = [1, 1, 2, 2, 2, 8]
chess_comp = list(int(i) for i in stdin.readline().split())

for i in range(len(chess)):
    print(chess[i] - chess_comp[i], end=" ")