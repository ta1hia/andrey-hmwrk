def insertion_sort(l):
    pv = 0

    while pv < len(l):
        next_in = pv
        while l[next_in] < l[next_in - 1] and next_in > 0:
            tmp = l[next_in - 1]
            l[next_in - 1] = l[next_in]
            l[next_in] = tmp
            next_in -= 1
        pv += 1

    return l


yo = [4,5,10,7,3,13,17,1]

print insertion_sort(yo)



