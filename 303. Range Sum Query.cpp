#include <vector>

class NumArray {
private:
    std::vector<int> prefixSum; 

public:
    NumArray(std::vector<int>& nums) {
        prefixSum = std::vector<int>(nums.size());
        prefixSum[0] = nums[0]; 

        for (int i = 1; i < nums.size(); i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }
    }

    int sumRange(int left, int right) {
        if (left == 0) {
            return prefixSum[right];
        }
        return prefixSum[right] - prefixSum[left - 1];
    }
};
