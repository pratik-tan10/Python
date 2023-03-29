#import sys
#sys.set_int_max_str_digits(0)

def fibonacci_last_digit(n):
    first = 0
    second = 1
    for i in range(2, n+1):
        first, second = second, (first + second)%10

    return second


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
