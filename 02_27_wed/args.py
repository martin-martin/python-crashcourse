# Arbitrary-length Arguments *args
def describe_pet(name, *args):
    print(f"this is {name}!")
    print('more info:')
    print(args[-1])
    for item in args:
        print(f"- {item}")


describe_pet('woofi', 'black', 'lice', 'barks')


# Keyword-Arguments **kwargs
def describe_pet(name, **kwargs):
    print(f"this is {name}!")
    for k, v in kwargs.items():
        print(f"{k} maps to {v}")
    print(kwargs)


describe_pet('woofi', color='black', says='barks')
