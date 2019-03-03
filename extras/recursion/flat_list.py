my_list = [1, 2, 3, [4, 3, [4, 7, [2, [8, 9]]], 5], [6, 7]]


# def unpack_list(nested_list, flat_list=[]):
#     for item in nested_list:
#         if type(item) == list:
#             flat_list = unpack_list(item, flat_list)
#         else:
#             flat_list.append(item)
#     return flat_list
#
#
# list_ = unpack_list(my_list)
# print(list_)

def unpack_list(nested_list, flat_list=[]):
    for item in nested_list:
        if type(item) == list:
            unpack_list(item)
        else:
            flat_list.append(item)
    return flat_list

list_ = unpack_list(my_list)
print(list_)


# for item in nested_list:
#     if type(item) == list:
#         for i in item:
#             flat_list.append(i)
#     else:
#         flat_list.append(item)
# print(flat_list)


# RECURSIVE WORKS WITH GLOBAL LIST
# flat_list = []
#
# def unpack_list(nested_list):
#     for item in nested_list:
#         if type(item) == list:
#             unpack_list(item)
#         else:
#             flat_list.append(item)

