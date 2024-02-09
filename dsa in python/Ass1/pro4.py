def prime(num):
    if num < 1:
        return False
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(N):
    prime_list = []
    num = 1  
    while len(prime_list) < N:
        if prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

N = 10 
primeno = primes(N)
print(primeno)
