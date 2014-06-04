def binary_search(L, k):
    mid = len(L)/2

    if len(L) > 1:
        if L[mid] < k:
            return binary_search(L[mid:], k)
        elif L[mid] > k:
            return binary_search(L[:mid], k)
    
    return L[mid] == k
