def prime_factorization(n):
    primfac = [] #all primes
    prim_fac = {} # dictionary that we gonna return
    
    # all primes
    i = 2
    while i**2 <= n:
        while (n % i) == 0:
            primfac.append(i) 
            n /= i
        i += 1
    
    if n > 1:
       primfac.append(int(n))
    
    # grouping the primes in a dictionary
    for i in set(primfac):
        prim_fac[i] = primfac.count(i)

    return prim_fac