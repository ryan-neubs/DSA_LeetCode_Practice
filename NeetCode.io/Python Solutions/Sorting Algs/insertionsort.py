def insertion_sort(items):
    if len(items) <= 1:
        return items

    for i in range(1, len(items)):
        curr = items[i]
        j = i-1
        while j >= 0 and curr < items[j]:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = curr
