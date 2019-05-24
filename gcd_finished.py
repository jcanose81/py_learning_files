# Euclids Algo

def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b

    return a

print(gcd(141, 282))  # should be 141
print(gcd(200, 150))  # should be 50
