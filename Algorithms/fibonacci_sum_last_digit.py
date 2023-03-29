def sum( dp, n, m ):
    ans = 0
    for i in range( 0, n+1 ):
        ans += dp[ i ]
        ans %= m
    return ans

def fibonacci( n, m ):
    dp = ( (6*m)+2 ) * [ 0 ]
    dp[ 0 ] = 0
    dp[ 1 ] = 1
    dp[ 2 ] = 1
    i = 3
    while i <= n and not ( dp[ i-2 ] == 0 and dp[ i-1 ] == 1 ):
        dp[ i ] = ( dp[ i-2 ] + dp[ i-1 ] ) % m
        i += 1
    p = i-2
    ans = sum( dp, n, m ) if n <= i-1 else sum( dp, n % p, m )
    return ans

if __name__ == '__main__':
    n = int( input() )
    m = 10
    ans = fibonacci( n, m )
    print( ans )