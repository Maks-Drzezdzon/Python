# https://leetcode.com/problems/remove-outermost-parentheses/submissions/ 75.15%



def removeOuterParentheses(S: str) -> str:
    result = ''
    stack = []
    store = ''
    
    for ele in S:
        if ele == '(':
            stack.append(ele)
        else:
            stack.pop()
        store += ele

        if not stack:
            result += store[1:-1]
            store = ''
            
    return result

print(removeOuterParentheses("((()))"))