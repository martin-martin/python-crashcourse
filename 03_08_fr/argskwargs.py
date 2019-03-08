def my_funct(name, *args):
    print("name is:", name)
    print(args[-1])
    for item in args:
        print(item)

my_funct('martin', 1, 4, 'hello', 'etc.')


def fun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} maps to {value}.")

fun(name="martin", number=1, greeting="hello")
