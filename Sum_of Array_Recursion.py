def fun(arr,n):
    if n==0:
        return 0
    else:
        return arr[n-1]+fun(arr,n-1)
arr  = [76,34,52,62]
n = len(arr)
result = fun(arr,n)
print("The Sum of Array Elements",result)