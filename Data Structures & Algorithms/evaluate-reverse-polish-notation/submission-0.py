class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def add(a, b):
            return a+b
        
        def sub(a, b):
            return a-b

        def mul(a, b):
            return a*b

        def div(a, b):
            return int(a/b)

        op_func = {
            "+" : add,
            "-" : sub,
            "*" : mul,
            "/" : div
        }

        stack = []

        for token in tokens:
            # if it's an operator
            if token in op_func:
                b = stack.pop()
                a = stack.pop()
                stack.append(op_func[token](a,b))

            # if it's a number
            if token not in op_func:
                stack.append(int(token))

        return stack[-1]