#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    nums_list = []
    n = int(input("Введите количество элементов списка: "))
    for i in range(n):
        item = float(input(f"Введите элемент {i + 1}: "))
        nums_list.append(item)

    negative_sum = sum([item for item in nums_list if item < 0])

    max_index = nums_list.index(max(nums_list))
    min_index = nums_list.index(min(nums_list))

    if max_index < min_index:
        max_index, min_index = min_index, max_index

    mult: int = 1

    for item in nums_list[min_index + 1:max_index]:
        mult *= item

    print("Сумма отрицательных элементов:", negative_sum)
    print("Произведение элементов между максимальным и минимальным:", mult)
