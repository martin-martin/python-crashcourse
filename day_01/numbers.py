# example of docstrings and PyCharm's "Go To... / Definition" and help() or .__dir__
def add_two_numbers(num1, num2):
    """adds two numbers.

    Args:
        num1 {int}: first number
        num2 {int}: second number
    Return:
        the_sum {int}: the sum of num1 plus num2
    """
    the_sum = num1 + num2
    return int(the_sum)


#print(add_two_numbers.__doc__)
#help(add_two_numbers)
