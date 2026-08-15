# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
# Problem     String Split and Join
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-15, 04:51 p.m.
# ──────────────────────────────────────────────────

def split_and_join(line):
    # write your code here
    split = line.split(" ")
    joined = "-".join(split)
    
    return joined

