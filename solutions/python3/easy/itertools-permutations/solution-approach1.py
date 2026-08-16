# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Problem     itertools.permutations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 09:15 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

[s,k] = input().split()
permutations = permutations(s, int(k))

sorted_perm = sorted("".join(x) for x in permutations)

for item in sorted_perm:
    print(item)
