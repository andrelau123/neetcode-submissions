class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        check = {}
        for letter in s:
            letters[letter] =   letters.get(letter, 0) + 1
        for letter in t:
            check[letter] = check.get(letter, 0) + 1
        if letters == check:
            return True
        else:
            return False

        

        