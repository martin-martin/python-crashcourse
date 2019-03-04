# DontSwear

# assuming this is user input
a = 2
b = '0'

ex = Exception('hello there')

try:
    result = a / b
except ZeroDivisionError as zde:
    print(f"can't divide by 0: {zde}")
except TypeError:
    raise ex
