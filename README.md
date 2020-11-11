# Merge Overlapping Intervals


## Definition of the task

Implement a function MERGE that receives a list of intervals and returns a list of intervals as the result. As a result, all overlapping intervals should be merged. All non-overlapping intervals are not affected.

Example:
Input: [25.30] [2.19] [14, 23] [4.8] Output: [2.23] [25.30]

## Solution

### Folder structure

```shellcript
dir MergeOverlappingIntervals
mergeIntervals.py
test_mergeIntervals.py
```

where
- mergeIntervals.py is the main python script which will be used to generate a list of intervals where overlapping intervals are merged.

### How to run the script

> Please use two terminals simultaneously

1. 

```console
cd MergeOverlappingIntervals
python mergeIntervals.py
```

2.

> How to pass arguments?
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



