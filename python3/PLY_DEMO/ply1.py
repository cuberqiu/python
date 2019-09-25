import ply.lex as lex

tokens = ["EQUAL", "DOT", "AND", "OR", "left", "right"]

def t_EQUAL(t):
    r'='
    print ("equal command received")
    return t

def t_DOT(t):
    r'\.'
    print("dot command received")
    return t

def t_AND(t):
    r'and'
    print("and command received")
    return t

def t_OR(t):
    r'or'
    print ("or command received")
    return t

def t_left(t):
    r'\('
    print("( command received")
    return t

def t_right(t):
    r'\)'
    print(") command received")
    return t

# 行号统计
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# 出错处理
def t_error(t):
    # print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# 测试数据
s = '''
from=101 and to=12 and (from_props.weight=80 or from_props.weight=10)
'''

# Give the lexer some input
lexer.input(s)

while True:
    tok = lexer.token()
    if not tok: break
    print(tok.value)