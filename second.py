# coding=utf-8
"""Домашнее  задание

Написать функцию find_multiples
Принимает два аргумента число и лимит
Возвращает таблицу умножения этого числа до лимита (включительно)
Например find_multiples(5, 25) вернет [5, 10, 15, 20, 25]
"""


def find_multiples(integer, limit):
    list_multiples = []
    for i in range(1, limit // integer + 1):
        list_multiples.append(integer * i)
    return list_multiples
