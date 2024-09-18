def is_prime(n):
    for i in range(1, (n//2)+1):
        if n % i == 0 and i != 1:
            return False
    return True

def get_primes(n):
    primeList = []
    for i in range(2, n):
        if is_prime(i):
            primeList.append(i)
    return primeList

def print_primes(n):
    primes = get_primes(n)
    for i in primes:
        print(i, end="\t")
    
