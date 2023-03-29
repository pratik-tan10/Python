def josephus(n,k):
    winner = 0
    for i in range(1, n+1):
        winner = (winner+k)%i
    return winner + 1


if __name__ == "__main__":
	n, k = map(int, input().split())
	print(josephus(n,k))
