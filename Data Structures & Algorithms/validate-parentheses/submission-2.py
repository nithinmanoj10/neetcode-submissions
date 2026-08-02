class Solution:
    def isValid(self, s: str) -> bool:
        para_stack = []
        open_para = ['(', '[', '{']
        close_para = {
            ')' : '(', 
            ']' : '[', 
            '}' : '{'
        }

        for para in s:
            if para in open_para:
                para_stack.append(para)
            elif para in close_para:
                if len(para_stack) == 0 or para_stack[-1] != close_para[para]:
                    return False
                else:
                    para_stack.pop()

        if len(para_stack) != 0:
            return False

        return True