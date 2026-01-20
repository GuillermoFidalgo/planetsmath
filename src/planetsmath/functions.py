# SPDX-FileCopyrightText: 2022 Fermi Research Alliance, LLC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations


def sum_function(list):
    """
    A function which takes a list as an argument and
    returns the sum

    Parameters
    ----------
    list: list
        Must be floats or ints

    Returns
    -------
    float:
        The sum of the elements in list
    """
    sum = 0.0
    for item in list:
        sum += item
    return sum


def print_hello():
    print("hello!")


def sum_product(lists):
    def print_hello():
        print("hello!")

    product = 1.0
    for item in lists:
        product *= item
    return product


def multiply_by_2(list):
    product = 2.0
    for item in list:
        item *= product
    return product


def division_function(list):
    """
    A function that takes a list and returns 1/the product of the elements

    Args:
        list(list): list of numbers

    Return:
         float: 1/the product
    """
    division = 1.0
    for item in list:
        division /= item
    return division
