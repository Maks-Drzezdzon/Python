    arr.sort()
    i=0
    for element in arr:
        if arr[len(arr) - i] == arr[len(arr)]:
            i +=1
        elif arr[len(arr) - i] != arr[len(arr)]:
            answer = arr[len(arr) - i]

    print (answer)
