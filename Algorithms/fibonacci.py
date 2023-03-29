import sys
sys.set_int_max_str_digits(0)

def fibonacci_number(n):
    fib = [0 for i in range(n+1)]
    if n > 0:
        fib[1] = 1
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]

    return fib[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
