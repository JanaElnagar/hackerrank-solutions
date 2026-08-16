# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
# Problem     Calendar Module
# Difficulty  Easy
# Subdomain   Date and Time
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-16, 09:51 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

[m,d,y] = input().split()

n = calendar.weekday(int(y),int(m),int(d))

print(calendar.day_name[n].upper())
