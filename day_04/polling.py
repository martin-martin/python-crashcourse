numbers = []



while True:
    number = int(input("please input a number"))
    numbers.append(number)

    if len(numbers) == 5:
        break

print(numbers)