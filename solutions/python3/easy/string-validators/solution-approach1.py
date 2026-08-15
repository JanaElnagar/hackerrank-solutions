# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
# Problem     String Validators
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-15, 05:17 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    s = input()
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
        
        
