# lambda expression
# anonymous function

my_list = [1, 3332, 3, 5, 42]


def square(x):
    return x**2

print(square(2))

sq = lambda x: x**2
print(sq(2))


squared_lam = list(map(lambda x: x**2, my_list))
squared_def = list(map(square, my_list))
print(squared_lam == squared_def)






















# def square(x):
#     return x**2
#
#
# sq = lambda x: x**2
#
# print(sq(3))
# print(square(3))
#
#
# lamb = lambda x: print(f"hei {x}")
#
# lamb("martin")
#
#
#
# # ---------
#
#
# my_list = [1, 2, 3, 5, 42]
#
# print(list(map(lambda x: x**2, my_list)))
# print(map(lambda x: x**2, my_list))
#
# this = map(lambda x: x**2, my_list)
# for i in this:
#     print(i)