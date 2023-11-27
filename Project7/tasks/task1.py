#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # region С использованием циклов
    # A = []
    # for i in range(10):
    #     element = int(input(f"Введите элемент {i + 1}: "))
    #     A.append(element)
    #
    # max_element = max(A)
    # max_index = A.index(max_element)
    #
    # A[0], A[max_index] = A[max_index], A[0]
    #
    # print("Преобразованный массив:", A)
    # endregion

    # region С использованием List Comprehensions
    A = [int(input(f"Введите элемент {i + 1}: ")) for i in range(10)]

    max_element = max(A)

    A_transformed = [max_element] + [x for x in A if x != max_element]

    print("Преобразованный массив:", A_transformed)
    # endregion


