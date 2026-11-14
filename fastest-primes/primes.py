import sys

def count_primes(n):
    if n < 2:
        return 0
    size = (n + 1) // 2  # odd numbers only: index i -> value 2*i+1
    sieve = bytearray(b"\x01") * size
    sieve[0] = 0  # 1 is not prime
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            start = i * i // 2
            sieve[start::i] = b"\x00" * ((size - 1 - start) // i + 1)
    return 1 + sum(sieve)  # +1 for the prime 2, not represented in the odd sieve

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        print(count_primes(int(data[0])))
