def opOrder(op1,op2):
    order_dic = {'*':4,'$':5,'/':4,'+':3,'-':3}
    if op1 == '(' or op2 == '(':
        return False
    elif op2 == ')':
        return True
    else:
        if order_dic[op1] < order_dic[op2]:
            return False
        else:
            return True

def infix2prefix(string):
    prefix = ''
    stack = []
    string_tmp = ''
    for s in string[::-1]:
        if s == '(':
            string_tmp += ')'
        elif s == ')':
            string_tmp += '('
        else:
            string_tmp += s
    for s in string_tmp:
        if s.isalpha():
            prefix = s + prefix
        else:
            while len(stack)  and opOrder(stack[-1],s):
                op = stack.pop()
                prefix = op + prefix
            if len(stack) == 0 or s != ')':
                stack.append(s)
            else:
                stack.pop()
    if len(stack):
        prefix = ''.join(stack) + prefix
    return prefix

if __name__ == '__main__':
    n=input()
    print(infix2prefix(n))
