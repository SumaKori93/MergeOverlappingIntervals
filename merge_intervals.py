# !/usr/bin/python
# coding=UTF-8
# Written by Suma Kori <suma.kori93@gmail.com>, November 2020

"""This script is used to perform merging of overlapping intervals.

- author: Suma Kori
- e-mail: suma.kori93@gmail.com
"""
from typing import List


class MergeIntervals:

    """ Class MergeIntervals"""

    def __init__(self, enable_user_input=True):
        self.enable_user_input = enable_user_input

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """This method receives a list of intervals and
        find the overlapping intervals and merge them

        :param: list
        """

        if len(intervals) == 0:
            return []

        # sort the intervals
        intervals.sort(key=lambda x: x[0])
        merged_list= []
        merged_list.append(intervals[0])
        for index in range(1, len(intervals)):
            last_element = merged_list[len(merged_list) - 1]
            if intervals[index][0] <= last_element[1]:
                last_element[1] = max(intervals[index-1][1], intervals[index][1])
                merged_list.pop(len(merged_list)-1)
                merged_list.append(last_element)
            else:
                merged_list.append(intervals[index])
        return merged_list

    def user_input(self):

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

        if len(elements) % 2 == 0:
            # How many elements each list should have
            count_list = int(input("How many elements each list should have?(please enter 2)"))
            # Using list comprehension
            final_intervals = [elements[i * count_list:(i + 1) * count_list] for i in range((len(elements) + count_list - 1)
                                                                                            // count_list)]
            print("Final list with chunk of size 2", final_intervals)
            print("Final merged output is:")

            return self.merge(final_intervals)

        else:
            return "please provide even number of elements"


def main(enable_user_input=True):
    """
    This method is to disable input capture when it is called from "test_merge_intervals.py"
    """
    print("enable_user_input", enable_user_input)
    if enable_user_input is False:
        obj1 = MergeIntervals(False)
    else:
        obj1 = MergeIntervals(True)
        print(obj1.user_input())


if __name__ == '__main__':
    main()
