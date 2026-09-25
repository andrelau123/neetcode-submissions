class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        nums.sort()
        answer = []
        for number in (nums):
            ans[number] = ans.get(number, 0) + 1
        sorted_ans = sorted(ans, key=ans.get)
        count = 0
        result = []
        while count < k:
            result.append(sorted_ans.pop())
            count += 1
        return result


        

                

        