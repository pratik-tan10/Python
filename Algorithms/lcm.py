def lcm(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)
        
    return int(a*b / gcd(a,b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

