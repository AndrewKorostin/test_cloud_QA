#Читает список чисел от пользователя и выводит только четные числа
def get_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers if even_numbers else "Четных чисел нет"

#Находит максимальное число из списка
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

#Находит минимальное число из списка
def find_min(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

#Сортирует список в порядке возрастания без использования встроенной функции sorted() - Пузырьковая сортировка
def custom_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# Ввод данных от пользователя
input_str = input("Введите числа через запятую: ")
if input_str:
    numbers = [int(num.strip()) for num in input_str.split(',')]

    # Вывод результатов
    print("Четные числа:", get_even_numbers(numbers))
    print("Максимальное число:", find_max(numbers))
    print("Минимальное число:", find_min(numbers))
    print("Отсортированный список:", custom_sort(numbers.copy()))
else:
    print("Строка пустая")