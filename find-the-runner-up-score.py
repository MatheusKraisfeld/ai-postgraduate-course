if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = arr[0]
    second = arr[0]
    
    for i in range(n):
        if arr[i] > first:
            first = arr[i]
            
    for i in range(n):
        if arr[i] > second and arr[i] != first:
            second = arr[i]
            
    print(second)
