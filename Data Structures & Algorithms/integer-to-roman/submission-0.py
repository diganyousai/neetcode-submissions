class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {0:('I','V'),1:('X','L'),2:('C','D'),3:'M'}
        nums = str(num)
        res = ''
        i,l = 0,len(nums)-1
        while l-i >= 0:
            if l-i == 3:
                res += dic[l-i]*int(nums[i])
            else:
                if int(nums[i]) < 4:
                    res += dic[l-i][0]*int(nums[i])
                elif int(nums[i]) == 4:
                    res = res + dic[l-i][0] + dic[l-i][1]
                elif int(nums[i]) == 5:
                    res += dic[l-i][1]
                elif 5 < int(nums[i]) < 9:
                    res = res + dic[l-i][1] + dic[l-i][0]*(int(nums[i])-5) 
                elif int(nums[i]) == 9:
                    if l-i == 2:
                        res = res + dic[l-i][0] + dic[l-i+1]
                    else:
                        res = res + dic[l-i][0] + dic[l-i+1][0]
            i += 1
        return res
                    


        


        