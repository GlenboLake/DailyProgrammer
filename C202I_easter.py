#!/c/Python27/python
# Determine when Easter is using the Gauss algorithm
import sys
from math import floor
from datetime import datetime


year = int(sys.argv[1])
a = year % 19
b = year % 4
c = year % 7
k = floor(year / 100)
p = floor((13 + 8 * k) / 25)
q = floor(k / 4)
M = (15 - p + k - q) % 30
N = (4 + k - q) % 7
d = (19 * a + M) % 30
e = (2 * b + 4 * c + 6 * d + N) % 7

try:
    easter = datetime(year, 3, int(22 + d + e))
except ValueError:
    easter = datetime(year, 4, int(d + e - 9))
print(easter.strftime('%B %d, %Y'))