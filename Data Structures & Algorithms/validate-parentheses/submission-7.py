class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i =='[' or i=='{':
                stack.append(i)
            elif i == ')':
                if stack !=[]:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                        break
                else:
                    return False
                    break
            elif i == ']':
                if stack !=[]:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                        break
                else:
                    return False
                    break
            elif i == '}':
                if stack !=[]:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                        break
                else:
                    return False
                    break
        if stack == []:
            return True
        else:
            return False
                    