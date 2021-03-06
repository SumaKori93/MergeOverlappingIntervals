# Merge Overlapping Intervals

Table of contents
- [Definition of the task](#definition-of-the-task)
- [Solution](#solution)
  * [Folder structure](#folder-structure)
  * [How to run the script](#how-to-run-the-script)

## Definition of the task

Implement a function MERGE that receives a list of intervals and returns a list of intervals as the result. As a result, all overlapping intervals should be merged. All non-overlapping intervals are not affected.

Example:
Input: [25.30] [2.19] [14, 23] [4.8] Output: [2.23] [25.30]

## Solution

### Folder structure

```shellcript
dir MergeOverlappingIntervals
merge_intervals.py
test_merge_intervals.py
```

where
- merge_intervals.py is the main python script which will be used to generate a list of intervals where overlapping intervals are merged.
- test_merge_intervals.py is the python script to test merge_intervals.py functions.

### How to run the script

> Please follow the below instructions

1. In terminal

```console
cd MergeOverlappingIntervals
python merge_intervals.py
```

2. How to pass Input?

```console
Enter the number of elements in list8
Enter numbers
25
30
2
19
14
23
4
8
[25, 30, 2, 19, 14, 23, 4, 8]
How many elements each list should have?(please enter 2)2
Final list with chunk of size 2 [[25, 30], [2, 19], [14, 23], [4, 8]]
Final merged output is:
[[2, 23], [25, 30]]
```

3. How to run test file?
```console
cd MergeOverlappingIntervals
pytest test_merge_intervals.py
```



