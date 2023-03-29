def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
