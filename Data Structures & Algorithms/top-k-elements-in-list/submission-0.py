class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = Counter(nums)
        
        return [num for num, count in frequencies.most_common(k)]

        