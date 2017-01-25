#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    a = 1;
    b = 2;
    total = 2
    while (b < n):
        tmp = a + b;
        if (tmp >=n):
            break;
        if (tmp %2 == 0):
            total += tmp;
        a = b;
        b = tmp;
    print total

