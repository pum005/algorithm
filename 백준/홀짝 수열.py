num = int(input())

total_ls = list(map(int, input().split()))

odd_ls =[]
even_ls = []

for n in total_ls:
    if n % 2 == 0:
        even_ls.append(n)
    else:
        odd_ls.append(n)

even_len = len(even_ls)
odd_len = len(odd_ls)
 
if num % 2 == 0:
    if even_len == (num /2) and odd_len == (num/2):
        print(1)
    else:
        print(0)
else:
    if even_len == (num //2) and odd_len == ((num //2) + 1):
        print(1)
    else:
        print(0)






