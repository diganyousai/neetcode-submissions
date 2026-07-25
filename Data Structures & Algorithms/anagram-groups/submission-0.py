class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}
        for i in strs:
            s=list(i)
            m=sorted(s)
            n=str(m)
            if n in hashmap:
                result[hashmap[n]].append(i)
            else:
                result.append([i])
                hashmap[n]=result.index([i])
        return result        