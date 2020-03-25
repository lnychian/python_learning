str = '((())(()(()))))('
i = 0
for s in str:
    if s == '(':
        i += 1
    elif s == ')':
        i -= 1
        if i < 0:
            print(False)
            break
if i == 0:
    print(True)