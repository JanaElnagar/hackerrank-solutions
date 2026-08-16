# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# Problem     Capitalize!
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 01:57 p.m.
# ──────────────────────────────────────────────────


def solve(s):
    x = s.split(' ')
    
    for i in range(len(x)):
        x[i] = x[i].capitalize()

    text = ' '.join(x)
    return text

