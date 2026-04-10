import random
import time

# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Генерация массива
def generate_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Замер времени
def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    end = time.time()
    return end - start

# Основной эксперимент
sizes = [100, 500, 1000, 2000]

print("Размер | Bubble Sort | Quick Sort")
print("-----------------------------------")

for size in sizes:
    arr = generate_array(size)

    bubble_time = measure_time(bubble_sort, arr)
    quick_time = measure_time(quick_sort, arr)

    print(f"{size:6} | {bubble_time:.5f} сек | {quick_time:.5f} сек")
