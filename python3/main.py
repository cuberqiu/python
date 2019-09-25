import sqlparse
import os

# print(sqlparse.format("select split('a,b,c,d', ',' as ret", reindent=True, strip_comments=True))

# print(sqlparse.format('select * from foo', reindent=True))

statement = sqlparse.format("select split('a,b,c,d', ',' as ret", reindent=True, strip_comments=True)

new_statment = []

for sql in sqlparse.parse(statement):
    _sql = str(sql).strip()
    if _sql:
        new_statment.append(_sql)

# print(new_statment)

p = sqlparse.parse(statement)[0]

# print(p.tokens)

# print(len(new_statment))
#
# for e in new_statment:
#     print(len(e))
#     print(e)


# print(os.path.join("/a", "b", "c"))
x = {"a":1}

for k,v in x.i



