class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prod = 1
        numberof0 = 0
        for number in nums:
            if number != 0:
             prod = prod * number
            # print(prod, "sdww")
            else:
                numberof0 += 1
       #print(prod, "dee")
        
        if numberof0 == 0:
            for i in range(len(nums)):
                ans.append(prod // nums[i])
        elif numberof0 == 1:
             for i in range(len(nums)):
                if nums[i] != 0:
                    ans.append(0)
                else:
                    ans.append(prod)
        else:
             for i in range(len(nums)):
                ans.append(0)
        return ans



            

        