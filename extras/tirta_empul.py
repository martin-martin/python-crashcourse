# encoding the Tirta Empul water ritual in code
pools = [range(1, 14), range(1, 3), range(1, 5)]


def cleanse(f_num, p_num):
    print(f"you are now at fountain {f_num} of pool {p_num}.")
    print("make a wish")
    print("splash your face " * 3)
    print("take a sip of water " * 3)
    print("hold your head under the fountain")
    print("say: 'thank you'")
    print("move on.\n")


for num, pool in enumerate(pools, start=1):
    if num == 1:
        skip = [1, 11, 12]
    elif num == 2:
        skip = []
    else:
        skip = [2, 3, 4]

    for fountain in pool:
        if fountain in skip:
            print(f"you are now at fountain {fountain} of pool {num}.")
            print("skip this one!\n")
        else:
            cleanse(fountain, num)

print("dry yourself off in the sunshine! you're all fresh and clean. :)")