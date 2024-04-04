# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        low = i + 1
        high = len(numbers) - 1
        target_check = target - numbers[i]
        while (low <= high):
            mid = (low + high) // 2
            if numbers[mid] == target_check:
                return [i + 1, mid + 1]
            if numbers[mid] < target_check:
                low = mid + 1
            else:
                high = mid - 1