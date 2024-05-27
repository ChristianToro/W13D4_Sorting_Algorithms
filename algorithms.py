def bubble_sort(arr):
    n = len(arr)
    bubb_count = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                bubb_count += 1
                swapped = True
       
        if not swapped:
            break

    return arr, bubb_count


array_1 = [64, 34, 25, 22, 12, 90, 11]
bubble_array, swap_count = bubble_sort(array_1)
print(f'Sorted array and count: {bubble_array}, {swap_count}')


def selection_sort(arr):
    n = len(arr)
    sel_count = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            sel_count += 1
    return arr, sel_count


array_2 = [64, 34, 25, 12, 22, 11, 90]
select_array, swap_count = selection_sort(array_2)
print(f'Sorted array and count: {select_array}, {swap_count}')


def insertion_sort(arr):
    ins_count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            ins_count += 1
        arr[j + 1] = key
        if j + 1 != i:
            ins_count += 1
    return arr, ins_count


array_3 = [90, 11, 25, 12, 22, 34, 64]
insert_array, swap_count = insertion_sort(array_3)
print(f'Sorted array and count: {insert_array}, {swap_count}')