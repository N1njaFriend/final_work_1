def filter_strings(arr):
    new_arr = []
    for string in arr:
        if len(string) <= 3:
            new_arr.append(string)
    return new_arr

arr = input("Введите элементы массива через запятую: ").split(",")
filtered_arr = filter_strings(arr)
print(filtered_arr)

# def filter_strings(arr):
#     new_arr = []
#     for string in arr:
#         if len(string) <= 3:
#             new_arr.append(string)
#     return new_arr

# arr1 = ["Hello", "2", "world", ":-)"]
# arr2 = ["1234", "1567", "-2", "computer science"]
# arr3 = ["Russia", "Denmark", "Kazan"]

# filtered_arr1 = filter_strings(arr1)
# print(filtered_arr1)  # Вывод: ["2", ":-)"]

# filtered_arr2 = filter_strings(arr2)
# print(filtered_arr2)  # Вывод: ["-2"]

# filtered_arr3 = filter_strings(arr3)
# print(filtered_arr3)  # Вывод: []