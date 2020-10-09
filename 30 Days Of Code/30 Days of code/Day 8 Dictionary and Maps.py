a = int(input())
count = dict()
for i in range(0, a):
    arr = input().split(' ')
    count[arr[0]] = arr[1]  # key as name value as number in dictionary
for i in range(100000):
    try:
        nam = str(input())
    except:
        break
    if nam in count:
        num = count[nam]
        print(nam+'='+str(num))
    else:
        print('Not found')
