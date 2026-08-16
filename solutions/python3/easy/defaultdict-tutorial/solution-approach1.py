# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
# Problem     DefaultDict Tutorial
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 10:14 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

[n,m] = input().split()
A = defaultdict(list)
for i in range(int(n)):
    A[input()].append(str(i+1))
    
for i in range(int(m)):
    x = input()
    if x in A.keys():
        print(" ".join(A[x]))
    else:
        print("-1")
