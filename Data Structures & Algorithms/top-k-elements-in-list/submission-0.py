class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequent = {}

        for i in nums:
            if i not in frequent:
                frequent[i] = 0
            if i in frequent:
                frequent[i] += 1

        sorted_f = dict(sorted(frequent.items(), key=lambda item: item[1], reverse=True))

        output = []

        i = 0
        while i < k:
            for key in sorted_f:
                if key not in output:
                    output.append(key)
                    break
            i += 1
        return output






        




        