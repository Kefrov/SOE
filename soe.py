def soe(x):
    res = []
    prime = [True] * (x + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, x):
        if prime[i]:
            res.append(i)
            if i ** 2 <= x:
                for j in range(2 * i, x, i): # O(nlog(log(n))) < O(nlogn)
                    prime[j] = False
                
    return res

print(soe(10 ** 8))
