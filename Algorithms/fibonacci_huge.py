def fibonacci_huge(n, m):
    dp = ((6*m) + 2) * [0]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    i = 3
    
    while i <=n and not (dp[i-2] == 0 and dp[i-1] == 1):
        dp[i] = (dp[i-1] + dp[i-2]) % m
        i += 1
    
    p = i - 2
    
    ans = dp[n] if n <= i - 1 else dp[n%p]
    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n,m))
