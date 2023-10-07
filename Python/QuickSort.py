def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose a pivot element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    input_list = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = quick_sort(input_list)
    print("Sorted array:", sorted_list)
