def sort_and_count_inversions(ip_list, left, right):
    if left < right:
        middle = int((left+right)/2)
        sort_and_count_inversions(ip_list, left, middle)
        sort_and_count_inversions(ip_list, middle+1, right)
        merge_and_count_split_inversions(ip_list, left, right, middle)
    
    elif left == right:
        return

def merge_and_count_split_inversions(ip_list, left, right, middle):
    global inversion_count
    temp = []
    i = left
    j = middle+1
    while i <= middle and j <= right:
        if ip_list[i] <= ip_list[j]:
            temp.append(ip_list[i])
            i += 1
        
        elif ip_list[i] > ip_list[j]:
            temp.append(ip_list[j])
            inversion_count += (middle-i+1)
            j += 1
    while i <= middle:
        temp.append(ip_list[i])
        i += 1
    while j <= right:
        temp.append(ip_list[j])
        j += 1
    j = 0
    for i in range(left,right+1):
        ip_list[i] = temp[j]
        j += 1

with open('IntegerArray.txt') as ip_file:
    ip_list = [int(line.rstrip()) for line in ip_file]

inversion_count = 0
sort_and_count_inversions( ip_list, 0 , len(ip_list) - 1 )
print('Inversion count: '+str(inversion_count))
