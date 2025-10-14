def compute_gcd(a, b):
    r = a - (b * (a//b))
    while r != 0:
        a = b
        b = r
        r = a - b * (a//b)

    return b


x = 99
y = 66
print("The GCD of", x, "and", y, "is", compute_gcd(x,y))
