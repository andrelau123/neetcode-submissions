class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += str(len(word))
            ans += "#"
            ans += word
        return ans


            


    def decode(self, s: str) -> List[str]:
        ans = []
        word = ""
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            number = int(s[i:j])
            word = s[j+1 : j+number +1]
            ans.append(word)
            i = j + 1+ number
        
        return ans                           

