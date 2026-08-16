# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# Problem     No Idea!
# Difficulty  Medium
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 09:30 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

[n,m] = input().split()
l = (int(x) for x in input().split())
a = set(int(x) for x in input().split())
b = set(int(x) for x in input().split())
happiness = 0

for n in l:
    if n in a:
        happiness += 1
    elif n in b:
        happiness -= 1
        
print(happiness)
