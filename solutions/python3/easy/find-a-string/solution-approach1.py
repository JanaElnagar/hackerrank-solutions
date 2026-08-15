# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Problem     Find a string
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-15, 05:05 p.m.
# ──────────────────────────────────────────────────

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count +=1
    
    return count
    
