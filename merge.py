# !/usr/bin/python
# coding=UTF-8
# Written by Suma Kori <suma.kori93@gmail.com>, November 2020

from itertools import islice

"""This script is used to perform merging of overlapping intervals.

- author: Suma Kori
- e-mail: suma.kori93@gmail.com
"""
from typing import List


class MergeIntervals:

    """ Class MergeIntervals"""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """This method receives a list of intervals and
        find the overlapping intervals and merge them

        :param: list
        """

        if len(intervals) == 0:
            return []

        # sort the intervals
        intervals.sort(key=lambda x: x[0])
        merged_list=[]
        merged_list.append(intervals[0])
        for i in range(1, len(intervals)):
            last_element = merged_list[len(merged_list) - 1]
            if intervals[i][0] <= last_element[1]:
                last_element[1] = max(intervals[i-1][1], intervals[i][1])
                merged_list.pop(len(merged_list)-1)
                merged_list.append(last_element)
            else:
                merged_list.append(intervals[i])
        return merged_list

    def userinput(self):

        """
        This method provides how to pass an entire list as command line
        argument.
        """
        elements = []
        number = int(input("Enter the number of elements in list"))
        print("Enter numbers")
        for i in range(number):
            data = int(input())
            elements.append(data)
        print(elements)

        # How many elements each list should have
        n = int(input("How many elements each list should have?(please enter 2)"))
        # Using list comprehension
        final_intervals = [elements[i * n:(i + 1) * n] for i in range((len(elements) + n - 1) // n)]
        print("Final list with chunk of size 2", final_intervals)
        print("Output:Merged list", self.merge(final_intervals))


obj1 = MergeIntervals()
print(obj1.userinput())



