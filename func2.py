
# setup function with 2 params
# greeting passed, name='You' default


def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


# using the parens runs 'hello_func'
# passed argument name='Matt' takes precedence
print(hello_func('YO', name='Matt'))
