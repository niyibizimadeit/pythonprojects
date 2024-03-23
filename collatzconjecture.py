def collatz(n):
    while n > 1:
        print(n, end=' ')
        if n%2:
            n = n*3+1
        else:
            n = n//2
    print(1, end='\n')


n = int(input("Enter n: "))
print('Sequence: ', end='')
collatz(n)
