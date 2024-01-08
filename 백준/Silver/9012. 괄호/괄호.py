import sys
# push
def stack_push(stack, value):
    stack.append(value)
# pop
def stack_pop(stack):
    last = stack.pop()
    return last

T = int(sys.stdin.readline())
for j in range(T):
    stack = []
    res = True
    s = sys.stdin.readline().strip()
    for i in range(len(s)):
        if s[i] == '(':
            stack_push(stack, '(')
        elif s[i] == ')':
            if len(stack) == 0:
                res = False
                break
            last = stack_pop(stack)
            if last == '(':
                continue
    if len(stack) != 0:
        res = False
    if res:
        print('YES')
    else:
        print('NO')