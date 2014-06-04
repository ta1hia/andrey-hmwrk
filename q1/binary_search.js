function binary_search (L, k) {
    console.log(L, k, mid);

    if (L.length > 1) {
        if (L[mid] > k) {
            return binary_search(L.slice(0, mid), k);
        } else if (L[mid] < k) {
            return binary_search(L.slice(mid, L.length), k);
        }
    }

    return (L[mid] == k)
}
