def mergesort(L):
    if len(L) == 1:
        return L

    pivot = len(L)/2
    left = mergesort(L[:pivot])
    right = mergesort(L[pivot:])

    L = merge(left, right)

    return L

def merge(l1, l2):
    A = []

    while l1 or l2: 
        if l1 and l2:
            n1, n2 = l1[0], l2[0]
            if n1 < n2:
                A.append(l1.pop(0))
            elif n2 < n1:
                A.append(l2.pop(0))
            else:
                A.append(l1.pop(0))
                A.append(l2.pop(0))
        elif l1 and not l2:
            A.extend(l1)
            l1 = []
        elif l2 and not l1:
            A.extend(l2)
            l2 = []

    return A



yo = [4,5,10,7,3,13,17,1]

print mergesort(yo)
