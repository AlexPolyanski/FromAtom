import random
from datetime import datetime


def find_max(arg):
    res_fnd_mx = 0
    for x in arg:
        if x > res_fnd_mx:
            res_fnd_mx = x
    return res_fnd_mx


def sum(arg):
    res_sum = 0
    for x in arg:
        res_sum += x
    return res_sum


def str_inverse(arg):
    print(__name__)
    return arg[::-1]


def benchmark(func):
    def deca(*args):
        start_time = str(datetime.now())
        func(*args)
        end_time = str(datetime.now())
        print(f"Скорость функции {func.__name__}: {end_time[20::]} - {start_time[20::]}")
    return deca


def multi(arg):
    res_mult = 1
    for x in arg:
        res_mult = x*res_mult
    return res_mult


def count_lit_reg(string):
    upper = 0
    low = 0
    for litteral in string:
        if litteral.isupper():
            upper += 1
        else:
            low += 1
    print(f"Символов в верхнем регистре: {upper}")
    print(f"Символов в нижнем регистре: {low}")


def count_fib_encl():
    x1 = 0
    x2 = 1

    def inner():
        nonlocal x1, x2
        x2, x1 = x1+x2, x2
        return x2
    return inner


def count_fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return count_fib_rec(n-1)+count_fib_rec(n-2)


def printGrocery(*args):
    gr_list = [i for i in args if type(i) == str and i != '' and i != ' ']
    if len(gr_list) > 0:
        print(gr_list)
    else:
        print('No products')


def printGroceries(*args):
    ls = [i for i in args if type(i) == str and i not in ('', ' ')]
    print('\n'.join([f'{num}) {i}' for num, i in enumerate(ls, 1)]) if ls else 'Нет продуктов')


@benchmark
def run_fib_recur(n):
    print(count_fib_rec(n))


@benchmark
def run_fib_encl(n):
    fib = count_fib_encl()
    for i in range(2, n+1):
        print(fib())


def change_global():
    animal = 'Стручок'
    print('After change global: ', animal)


animal = 'Кот'
change_global()

# printGrocery('Бананы', [1, 2], ('Python',), 'Яблоки', '', 'Макароны', 5, True, 'Кофе', False)
# string = 'BlacK Cat GOING'
# count_lit_reg(string)
# printGroceries([4], {}, 1, 2, {'Mathlab'}, '', '  ')
# printGrocery([4], {}, 1, 2, {'Mathlab'}, 'Кукан')

# random_list = [random.randint(1, 100) for _ in range(10)]
# print(random_list)
# print(find_max(random_list))
# print(sum(random_list))
# print(multi(random_list))
