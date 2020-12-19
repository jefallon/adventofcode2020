def input_to_list(infile):
    expressions = []
    with open(infile, 'r') as f:
        for row in f:
            expressions.append(row.strip().split())
    return expressions

def evaluate(expression):
    opens = []
    closes = []
    for idx,term in enumerate(expression):
        if term.startswith('('):
            for char in term:
                if char == '(':
                    opens.append(idx)
                else:
                    break
        elif term.endswith(')'):
            for char in term[::-1]:
                if char == ')':
                    closes.append(idx)
    if len(opens) == 0:
        expr_val = int(expression.pop(0))
        for idx, term in enumerate(expression):
            if term == '+':
                expr_val += int(expression[idx + 1])
            elif term == '*':
                expr_val *= int(expression[idx + 1])
        return expr_val
    last_open = opens.pop(-1)
    for idx, rparen in enumerate(closes):
        if rparen > last_open:
            paired_close = closes.pop(idx)
            break
    new_expr_lead = expression[:last_open]
    if paired_close < len(expression) - 1:
        new_expr_tail = expression[paired_close+1:]
    else:
        new_expr_tail = []
    split_open = expression[last_open].split('(')
    split_close = expression[paired_close].split(')')
    new_mid_val = evaluate(split_open[-1:]+expression[last_open+1:paired_close]+split_close[:1])
    if len(split_open) > 2:
        new_expr_mid = ['('*(len(split_open) - 2)+str(new_mid_val)]
    elif len(split_close) > 2:
        new_expr_mid = [str(new_mid_val)+')'*(len(split_close)-2)]
    else:
        new_expr_mid = [str(new_mid_val)]
    new_expr = new_expr_lead + new_expr_mid + new_expr_tail
    return evaluate(new_expr)

if __name__ == '__main__':
    infile ='Advent18.txt'
    expressions = input_to_list(infile)
    evaluated = [evaluate(expression) for expression in expressions]
    print(sum(evaluated))