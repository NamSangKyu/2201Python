def check_prime_number(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for n in range(1,101):
    if check_prime_number(n):
        print(n,end=" ")
