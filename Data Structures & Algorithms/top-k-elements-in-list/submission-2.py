class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in sorted_count[:k]]