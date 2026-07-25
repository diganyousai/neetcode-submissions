class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap =Counter(nums)
        s = list(hashmap.values())
        m=sorted(s)
        output=[]
        for i  in hashmap:
            if hashmap[i] in m[(len(m)-k):len(m)]:
                output.append(i)
        return output

        