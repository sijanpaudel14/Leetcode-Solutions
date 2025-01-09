class Solution:
    def permute(self, nums):
        result = []  # This list will hold all the permutations.

        # Base case: If there's only one number in the list, return it as the only permutation.
        if len(nums) == 1:
            return [nums[:]]  # Return a copy of `nums` wrapped in a list.

        # Loop through each element in the `nums` list.
        for i in range(len(nums)):
            # Remove the first element of the list and store it in `n`.
            n = nums.pop(0)

            # Recursively call `permute` to get all permutations of the remaining numbers.
            perms = self.permute(nums)

            # For each permutation returned, add the removed element (`n`) to the end.
            for perm in perms:
                perm.append(n)

            # Extend the result list with the updated permutations.
            result.extend(perms)

            # Restore the removed element (`n`) back to the end of the list.
            # This ensures the original list remains intact for the next iteration.
            nums.append(n)

        # Return the list of all generated permutations.
        return result
