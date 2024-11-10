class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        # Base case (return single item in list).
        if len(nums) == 1:
            return [nums[:]]
            
        # For as the length of the original list the first item will be popped and permutations will be made with the remainig items.
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            # The item popped is now appended to the smaller total permutations.
            for perm in perms:
                perm.append(n)

            # Extend new permutations and append the item that was popped.
            result.extend(perms)
            nums.append(n)

        return result
    
