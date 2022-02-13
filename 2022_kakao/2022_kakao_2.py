
def get_n_base(n, k):
    n_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        n_base += str(mod)
    return n_base[::-1]

def get_prime_pattern(n_base):
    cndd_prime = n_base.split('0')
    prime_pattern = []
    for prime in cndd_prime:
        if prime == '':
            continue
        if int(prime) > 1:
            prime_pattern.append(int(prime))
    return prime_pattern

def is_prime(n):
    i = 2
    while n > i:
        if n % i == 0:
            return False
        i += 1
    return True

def solution(n, k):
    answer = 0
    n_base = get_n_base(n, k)
    cndd_prime_list = get_prime_pattern(n_base)
    for cndd_prime in cndd_prime_list:
        answer += is_prime(cndd_prime)
    return answer


print(solution(110003, 10))