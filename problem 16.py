def solve (n):
    m=2**n
    l=0
    k=1
    while m > 0 :
        h=m%(10**k)
        l+=(h/10**(k-1))
        k+=1
        m=m-h
    return l
    
assert solve(15) == 26

print(solve(1000))

