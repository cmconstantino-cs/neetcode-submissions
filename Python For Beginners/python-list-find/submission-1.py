from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    n = -1 
    for element in nums:
        n += 1
        if element == target:
            result = n
            break
        else:
            pass
    return result



# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

