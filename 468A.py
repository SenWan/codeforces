n = int(input())
if(n % 2 == 0):
    n = n / 2
else:
    n = ((n + 1) // 2) * (-1)
print(int(n))