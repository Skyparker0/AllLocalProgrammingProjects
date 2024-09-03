# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:52:34 2021

@author: batte
"""


import math, itertools
def compute():
    LIMIT = 10**9
    ans = 0
    # What search range do we need?
    # c = (s^2+t^2)/2. Perimeter = p = 3c +/- 1 = 3/2 (s^2+t^2) +/- 1 <= LIMIT.
    # We need to keep the smaller perimeter within limit for
    # the search to be meaningful, so 3/2 (s^2+t^2) - 1 <= LIMIT.
    # With t < s, we have that s^2+t^2 < 2s^2, so 3/2 (s^2+t^2) - 1 < 3s^2 - 1.
    # Therefore it is sufficient to ensure that 3s^2 - 1 <= LIMIT, i.e. s^2 <= (LIMIT+1)/3.
    for s in itertools.count(1, 2):
        if s * s > (LIMIT + 1) // 3:
            break
        for t in range(s - 2, 0, -2):
            if math.gcd(s, t) == 1:
                a = s * t
                b = (s * s - t * t) // 2
                c = (s * s + t * t) // 2
                if a * 2 == c - 1:
                    p = c * 3 - 1
                    if p <= LIMIT:
                        ans += p
                        print(c,c,c-1)
                if a * 2 == c + 1:
                    p = c * 3 + 1
                    if p <= LIMIT:
                        ans += p
                        print(c,c,c+1)
                # Swap the roles of a and b and try the same tests
                # Note that a != b, since otherwise c = a * sqrt(2) would be irrational
                if b * 2 == c - 1:
                    p = c * 3 - 1
                    if p <= LIMIT:
                        ans += p
                        print(c,c,c-1)
                if b * 2 == c + 1:
                    p = c * 3 + 1
                    if p <= LIMIT:
                        ans += p
                        print(c,c,c+1)
    return str(ans)