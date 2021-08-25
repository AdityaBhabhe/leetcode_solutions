 # Question 1/176 Contains Duplicate

 def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

# Question 2/176 Missing Number
def missingNumber(self, nums: List[int]) -> int:
    for i in range(0,len(nums)+1):
        if i in nums:
            i += 1
        else:
            return i            

# Question 3/176 Find all numbers disppeared in an array
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        n = []
        for i in range(1,len(nums)+1):
            if i in s:
                i += 1
            else:
                n.append(i)
        return n 