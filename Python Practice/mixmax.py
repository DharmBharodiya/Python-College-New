def minmaxFinder(arr, low, high):
    if low == high:
        return (arr[low], arr[high])

    if high == low + 1:
        if(arr[low] < arr[high]):
            return (arr[low], arr[high])
        else:
            return (arr[high], arr[low])

    mid = (low + high) //2

    min1, max1 = minmaxFinder(arr, low, mid)
    min2, max2 = minmaxFinder(arr, mid+1, high)

    finalMin = min(min1, min2)
    finalMax = max(max1, max2)

    return (finalMin, finalMax)

arr = [5,3,1,77,4]
n = len(arr)

min, max = minmaxFinder(arr, 0, n - 1)
print(f"Minimum: {min} Maximum: {max}")