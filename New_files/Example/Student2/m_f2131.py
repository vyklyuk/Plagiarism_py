#!/usr/bin/env python
#coding: utf8


def safe_div(x, y):
    """
    Do a safe division :-)
    for fun and profit
    """
    if y != 0:
        z = x / y
        return z
    else:
        print "Yippie-kay-yay, motherf___er!"


def gcd(a, b):
   """
   Нахождение НОД
   """
   while a != 0:
      a,b = b%a,a # параллельное определение
   return b

def list_sum(*args):
    smm = 0
    for arg in args:
        smm += arg
    return smm

k=safe_div(10, 2)
print k
print safe_div.__doc__

k=gcd(100, 60)
print k


my_f=gcd
print my_f(99, 3)

print list_sum(1,2,3,4,5,6,7,8,9)
lst = [1, 10, 2]
print list(range(*lst))


# наступний приклад база даних
def enquote1(in_str):
    """Quotes input string with single-quote"""
    in_str = in_str.replace("'", r"\'")
    return "'%s'" % in_str

def enquote2(in_str):
    """Quotes input string with double-quote"""
    in_str = in_str.replace('"', r'\"')
    return '"%s"' % in_str

def gen_insert(table, **kwargs):
    """Generates DB insert statement"""
    cols = []
    vals = []
    for col, val in kwargs.items():
        cols.append(enquote2(col))
        vals.append(enquote1(str(val)))
    cols = ", ".join(cols)
    vals = ", ".join(vals)

    return 'INSERT INTO "%s"(%s) VALUES(%s);' % (
            table, cols, vals)
