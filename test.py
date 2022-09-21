def foo(a):
    a = a+5
    print(a)


codes = [10, 20, 30, 40, 50]
values = ['bandits', 'jerk', 'mashrooms', 'pharma', 'cock']
oper_dict = dict(zip(codes, values))
numbers = [121, 544, 111, 99, 77]
eleven_remains = [x for x in numbers if x % 11 == 0]
# print(eleven_remains)
squares = {x: x*x for x in range(10)}
# print(squares)
odd = set()
odd = {val for val in range(10) if val % 2 != 0}
# print(odd)
tupple_keys = ('optimist', 'pessimist', 'troll')
tupple_values = ('hlf_full', 'hlf_emty', 'fck_off')
glass = {k: v for k, v in zip(tupple_keys, tupple_values)}
# print(glass)

a = 10
foo(a)
print(a)
