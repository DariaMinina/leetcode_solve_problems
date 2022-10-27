https://walkccc.me/LeetCode/problems/0022/

# 356. Line reflection

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.
Учитывая n точек на 2D-плоскости, найдите, существует ли такая линия, параллельная оси y, которая отражает данные точки.

Example 1: Given points = [[1,1],[-1,1]], return true.

Example 2: Given points = [[1,1],[-1,-1]], return false.

Follow up: Could you do better than O(n2)?

Hint:

Find the smallest and largest x-value for all points. If there is a line then it should be at y = (minX + maxX) / 2. For each point, make sure that it has a reflected point in the opposite side.

# 228. Summary Ranges

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

**Example 1:**
```text
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

**Example 2:**
```text
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

# 281. Zigzag Iterator 

Given two 1d vectors, implement an iterator to return their elements alternately.

**Example:**

```text
Input:
v1 = [1,2]
v2 = [3,4,5,6] 


Output: [1,3,2,4,5,6]

Explanation: By calling  next repeatedly until hasNext returns false, the order of elements returned by next
should be: [1,3,2,4,5,6].
```

# String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

**Example 1**:

```text
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
```

# 206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

```text
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

# 22. Generate Parentheses 

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1**:

```text
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2**:

```text
Input: n = 1
Output: ["()"]
```