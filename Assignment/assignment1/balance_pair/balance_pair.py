def balance_pair(brackets: str) -> bool:
    if not brackets or len(brackets) % 2 == 1:
        return False
    stack = []
    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        elif bracket in "}])":
            peek = stack[-1]

            if peek == "{" and bracket == "}":
                stack.pop()
            elif peek == "[" and bracket == "]":
                stack.pop()
            elif peek == "(" and bracket == ")":
                stack.pop()
            else:
                return False
        else:
            return False

    return not stack


print(balance_pair("[]{}{{1"))
