# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Problem     Word Order
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 09:43 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n = int(input())
words = defaultdict(int)

for i in range (n):
    word = input()
    words[word] += 1
    
print(len(words))
for value in words.values():
    print(value,end=" ")
