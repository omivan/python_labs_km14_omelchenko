# ВАШ КОД ТУТ
def rrange(begin, end, step = 1):
    if((begin - end) * step >= 0 ): return list()
    my_list = list()
    my_list.append(begin)
    my_list.extend(rrange(begin + step, end, step))
    
    return my_list

# ПЕРЕВІРКА
x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
#print(x, y, z)
print(x)
print(y)
assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')