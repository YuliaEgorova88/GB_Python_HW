
n = int(input('Введите число N: '))
index_list = [2, 4, 3, 1, 8]  # int(i) for i in input().split()
summ = 1
requested_num = [i for i in range(-n, n + 1)]
print(requested_num)
print(index_list)

for i in range(len(requested_num)): 
    for j in index_list:
        if i == j:
            summ *= requested_num[i]              
print(abs(summ))           # -3, -1, -2, -4, 3
        

