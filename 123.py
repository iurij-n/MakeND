d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

def foo1():
    d['a'] = 777


def foo2():
    print(d)

fff = {}
fff['a']=78
print(fff)
foo1()
foo2()

def format_data(data):
    data = [symbol for symbol in data]
    # data = data[8:] + data[5:7] + data[0:4]
    print(f'{"".join(data[8:])}.{"".join(data[5:7])}.{"".join(data[:4])}')


format_data('2022-08-17')
    