# find the greatest common denominator of two numbers
# using Euclid's Algorithm


def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b  # gives the remainder of division with modulus operator

    return a


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))  # should be 4
