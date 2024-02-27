def selection_sort(array, size):
    arr = array
    for i in range(size - 1):
        min_element = arr[i]
        min_index = i

        for j in range(i + 1, size):
            if arr[j] < min_element:
                min_element = arr[j]
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr




def bucket_sort(array, length):
    largest = max(array)
    size = largest / length

    buckets = [[] for i in range(length)]

    for i in range(length):
        index = int(array[i] / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])

    for i in range(len(array)):
        buckets[i] = sorted(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result

def bead_sort(input_list, size):
    return_list = []
    transposed_list = [0] * max(input_list)
    for num in input_list:
        transposed_list[:num] = [n + 1 for n in transposed_list[:num]]
    for i in range(size):
        return_list.append(sum(n > i for n in transposed_list))
    return return_list

