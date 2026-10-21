class Solution:
    def isPalindrome(self, s: str) -> bool:
        pt1 = 0
        pt2 = len(s) -1
        s = s.lower()
        while pt1 < pt2:
            print(s[pt1], s[pt2])
    
            if not s[pt1].isalnum():
                print("F")
                pt1 += 1
            elif not s[pt2].isalnum():
                print("d")
                pt2 -= 1
            elif s[pt1].isalnum() and s[pt2].isalnum():
                if s[pt1] != s[pt2]:
                    print("ff")
                    return False
                else:
                    pt1 +=1
                    pt2 -= 1
                    print("succ")
        return True
            
        
        
        