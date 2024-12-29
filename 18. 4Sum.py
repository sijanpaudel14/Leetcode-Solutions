class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()  # Step 1: Sort the array
        result = []
        n = len(nums)

        # Step 2: Iterate over the first number
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first number
                continue

            # Step 3: Iterate over the second number
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates for the second number
                    continue

                # Step 4: Two pointers for the remaining two numbers
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for the third and fourth numbers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move pointers after finding a valid quadruplet
                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1  # Need a larger sum
                    else:
                        right -= 1  # Need a smaller sum

        return result
