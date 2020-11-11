# !/usr/bin/python
# coding=UTF-8
# Written by Suma Kori <suma.kori93@gmail.com>, November 2020

"""This script is used to perform test cases on MergeIntervals.

- author: Suma Kori
- e-mail: suma.kori93@gmail.com
"""

from MergeOverlappingIntervals import merge_intervals


def test_merge_success():

    """This method is used to test if the merging is success"""
    x = [[25, 30], [2, 19], [14, 23], [4, 8]]
    sc = merge_intervals.MergeIntervals()
    test_merge_interval = sc.merge(x)
    assert test_merge_interval == [[2, 23], [25, 30]]

def test_merge_fail():

    """This method is used to test if the merging is success"""
    x = [[25, 30], [2, 19], [14, 23], [4, 8]]
    sc = merge_intervals.MergeIntervals()
    test_merge_interval = sc.merge(x)
    assert test_merge_interval != [[14, 23], [25, 30]]


