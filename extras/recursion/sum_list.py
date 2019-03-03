'''
Sum up all elements from the nested list of integers below.

'''

list_ = [1, 2, [10, 11], [42, 3], 9]

nlsum = 0
for item in list_:
    if type(item) == list:
        #print(item)
        nlsum += sum(item)
    else:
        nlsum += item

print(nlsum)

# - different solution -

flat_list = []
for i in list_:
    if isinstance(i, list):  # if type(i) == list:
        for j in i:
            flat_list.append(j)
    else:
        flat_list.append(i)

print(flat_list)



# ----- recursive solution -----

def list_add(nested_list, nlsum):
    for item in nested_list:
        if type(item) == list:
            # print(item)
            nlsum = list_add(item, nlsum)  # we call the function recursively
        else:
            nlsum += item
    return nlsum  # base case, gotta return something for the call to eventually end

res = list_add(list_, 0)
print(res)
