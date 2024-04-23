'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

eg:- 
nums = [2, 7, 11, 15] target = 9, return [0, 1]
nums = [3, 2, 4] target = 6, return [1, 2]
nums = [3, 3] target = 6, return [0, 1]
'''


from typing import List


def twoSumBruteForce(nums: List[int], target: int) -> List[int]:
    '''
    Complexity -> O(n^2)
    Loop through each item while adding it to 
    subsiquent items and comparing if they are 
    equal to the target, return the indices in original array
    '''
    for index, n in enumerate(nums):
        for i in nums[index+1:]:
            if n + i == target:
                return [nums.index(n), nums.index(i)]


print('Brute force solutions')
print(twoSumBruteForce([2, 7, 11, 15], 9))  # [0, 1]
print(twoSumBruteForce([3, 2, 4], 6))  # [1, 2]
print(twoSumBruteForce([3, 3], 6))  # [0, 1]
print('\n')


def twoSum(nums: List[int], target: int) -> List[int]:
    '''
    Complexity -> O(n)
    Compare difference of target and value,
    check if the difference already in hashmap
    return indices of difference and value
    else: add value and its coresponding index to hashmap
    '''
    hashMap = {}  # value : index

    for i, n in enumerate(nums):
        diff = target - n

        if diff in hashMap:
            return [hashMap[diff], i]

        hashMap[n] = i

    return


print('Optimised solutions')
print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(twoSum([3, 2, 4], 6))  # [1, 2]
print(twoSum([3, 3], 6))  # [0, 1]
