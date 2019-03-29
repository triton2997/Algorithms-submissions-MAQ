import sys

def swap(a, i, j):
    if i!=j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

def choose_pivot(a, left, right):
    global METHOD
    if METHOD == 1:
        return left
    elif METHOD == 2:
        return right
    elif METHOD == 3:
        middle = left + int( (right - left)/2 )
        vals = [a[left], a[middle], a[right]]
        indices = [left, middle, right]
        vals_indices = zip(vals,indices)
        median_value = sum(vals) - max(vals) - min(vals)
        for i, j in vals_indices:
            if median_value == i:
                return j

def partition(a, left, right):
    pivot = choose_pivot(a, left, right)
    swap(a, pivot, left)
    pivot = left
    global no_of_comparisons
    no_of_comparisons += (right-left)
    i = left + 1
    j = left + 1
    while j <= right:
        if a[j] < a[pivot]:
            swap(a, i, j)
            i += 1
        j += 1
    swap(a, pivot, i-1)
    pivot = i-1
    return pivot

def quicksort(a, left, right):
    if right - left+1 <= 1:
        return
    else:
        pivot = partition(a, left, right)
        quicksort(a, left, pivot-1)
        quicksort(a, pivot+1, right)


no_of_comparisons = 0

METHOD = 1
METHOD = int(sys.argv[1])

with open('QuickSort.txt') as ip_file:
    ip_list = [int(line.rstrip()) for line in ip_file]

quicksort(ip_list, 0, len(ip_list)-1)

print(no_of_comparisons)
