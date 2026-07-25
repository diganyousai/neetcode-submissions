class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashdict1 = {}
        hashdict2 = {}
        def junge(x: str, hashdict: dict) -> dict:
            for i in x:
                if i not in hashdict:
                    hashdict[i] = 1
                else:
                    hashdict[i] +=1
            return hashdict
        result1 = junge(s , hashdict1)
        result2 = junge(t , hashdict2)
        if result1 == result2:
            return True
        else:
            return False

        