# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Problem     itertools.product()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 09:01 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
from itertools import product

A = list(input().split())
B = list(input().split())

str_product = product(A,B)
int_product = [tuple(int(item) for item in row) for row in str_product]

for item in int_product:
    print(item,end=" ")
