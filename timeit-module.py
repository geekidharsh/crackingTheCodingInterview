# Measure execution time of small code snippets¶
import timeit

a = timeit.timeit('"-".join(str(n) for n in range(100))', number=50000)
b = timeit.timeit('"-".join([str(n) for n in range(100)])', number=100000)
c = timeit.timeit('"-".join(map(str, range(100)))', number=200000)
print(a,b,c)