#/usr/bin/env python3
import sys
def prime_factor(n):
    if n <= 3:
        return int(n)
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        for i in range(5, int((n)**0.5) + 1, 6):
            if ((n % i) == 0):
                return int(i)
            if (n % (i + 2) == 0):
                return prime_factor(n/(i+2))
    return int(n)


print(prime_factor(int(sys.argv[1])))
