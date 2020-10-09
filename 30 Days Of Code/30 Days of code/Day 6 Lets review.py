# breaking string into odd even position
n = int(input())

for i in range(n):
    arr = input()
    # print(arr)
    # print(arr[0])

    for j in range(0, len(arr), 2):
        # if j%2 ==0:
        print(arr[j], end='')
    print(' ', end='')
    for j in range(1, len(arr), 2):
        # if j%2 != 0:
        #even += arr[j]
        print(arr[j], end='')
    print('\n', end='')
