#!/bin/python

import sys

def get_seive(num):    
    num_items = (num - 1) /2
    limit = long((num)** 0.5 - 1)/ 2
    
    seive = [False] * (num_items)
        
    for i in xrange (0, limit):
        if not seive[i]:
            for i in xrange(2 * (i + 1) * (i + 2) - 1, num_items, 2 * (i + 1) + 1):
                seive[i] = True
    return seive

def list_prime(seive):
    return [2*(i + 1) + 1 for i, val in enumerate(seive) if not val]
    
def compute_sum(primes, n):
    prime_sum = [0] * n
    prime_sum[0] = 0
    prime_sum[1] = 2
    j = 0;
    for i in xrange(2, n):
        if (primes[j] > (i + 1)):
            prime_sum[i]= prime_sum[i - 1]
        else:
                prime_sum[i]= prime_sum[i - 1] + primes[j]
                j = (j + 1 if j < len(primes) - 1 else j)
    return prime_sum              

limit = 1000000
seive = get_seive(limit)
all_primes = list_prime(seive)
sum_of_primes = compute_sum(all_primes, limit)
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print sum_of_primes[n - 1]
