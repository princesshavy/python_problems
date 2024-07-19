import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a = 48
b = 18
print("LCM of", a, "and", b, "is:", lcm(a, b))