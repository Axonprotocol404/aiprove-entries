# Fastest correct prime counter

Reads an integer N (1 ≤ N ≤ 5,000,000) on stdin, prints the count of
primes ≤ N on stdout.

**Run command:** `python3 primes.py`

Implementation: odd-only sieve of Eratosthenes over a `bytearray`, with
bulk slice-assignment marking (no per-element Python loop) — π(5,000,000)
= 348513 in ~0.1 s on commodity hardware. Correctness first: the sieve is
exact, verified against known values π(10)=4, π(100)=25, π(1000)=168,
π(10^6)=78498, π(5·10^6)=348513.
