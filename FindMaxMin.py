array = list(map(int,input().strip().split()))
max_int = array[0]
min_int = array[0]

for i in range(1,len(array)):
    if array[i] > max_int:
        max_int = array[i]
    if array[i] < min_int:
        min_int = array[i]
print(max_int - min_int)