"""
"""

class Function(object):

    def __init__(self, name, body):
        self.name = name.replace('$', '')
        self.body = body

    def call(self, arg, env):
        env[self.name] = arg
        return _evaluate(self.body, env)

    def __repr__(self):
        return '$%s.%s' % (self.name, self.body)


def evaluate(ast, env={}):
    return _evaluate(ast, env)


def _evaluate(ast, env={}):
    ## If not List
    if type(ast) == str:
        try:
            ast = env[ast]
            return _evaluate(ast)
        except KeyError:
            return ast

    if type(ast) == Function:
        return ast

    ## If list
    if len(ast) == 1:
        return _evaluate(ast[0])

    key = ast[0]

    if type(key) == str:
        if key[0] == '$':
            return Function(key, ast[1:])

        try:
            key = _evaluate(env[key])
        except KeyError:
            pass

    if type(key) == Function:
        return key.call(ast[1], env)

    return _evaluate([_evaluate(key)] + ast[1:])
