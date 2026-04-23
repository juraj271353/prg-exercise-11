import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)

    for i in range(n):
        smallest = i

        for j in range(i, n):
            if numbers[j] < numbers[smallest]:
                smallest = j

        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

    return numbers


def bubble_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers



def main():
    print(selection_sort([5, 1, 4, 2, 8]))
    print(selection_sort(random_numbers(20)))

    print(bubble_sort([5, 1, 4, 2, 8]))
    print(bubble_sort(random_numbers(20)))