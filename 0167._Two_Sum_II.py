class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(numbers)-1
        sum=numbers[left]+numbers[right]
        
        while left<right:
            if sum<target:
                left= left+1
                sum=numbers[left]+numbers[right]
            elif sum>target:
                right= right-1
                sum=numbers[left]+numbers[right]
            elif sum==target:
                return [left+1,right+1]