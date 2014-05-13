"""
<name> := Any none spaced thing
<function> := $<name>.<body>
<application> := (<function expression> <argument expression>)

"""
def parse(source):
    source = source.strip()
    return _parse(source)


def _parse(source):
    parsed = []
    if source[0] == '$':
        name, body = _parse_function(source)
        parsed.append(name)
        parsed.append(body)
    elif source[0] == '(':
        func_exp, arg_exp = _parse_application(source)
        parsed.append(func_exp)
        parsed.append(arg_exp)
    else:
        parsed.append(source)
    if len(parsed) == 1:
        return parsed[0]
    return parsed


def _parse_function(exp):
    name, body = exp.split('.', 1)
    return name, _parse(body)


def _parse_application(exp):
    inner_exp = exp[1:-1]
    func_exp, arg_exp = split_on_space(inner_exp)
    return _parse(func_exp), _parse(arg_exp)


def split_on_space(exp):
    pos = 0
    end = len(exp)
    open_paren = 0
    while pos < end:
        if exp[pos] == '(':
            open_paren += 1
        elif exp[pos] == ')':
            open_paren -= 1
        elif exp[pos] == ' ' and open_paren == 0:
            return exp[0:pos].strip(), exp[pos:].strip()

        pos += 1
    return exp
