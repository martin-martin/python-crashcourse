books = ['not_here.txt', 'war_and_peace.txt', 'recipe.txt']


# SUCCESFUL SITUATION: try -> else -> finally
# UNSUCCESFUL SITUATION: try -> except -> finally

for book in books:
    try:
        # object as variable_name
        # variable_name = object
        fin = open(book, 'r')

    except FileNotFoundError as fnf:
        # with open('error.log', 'a') as log:
        #     log.write(f"{fnf} has occured\n")
        print(f"sorry, this file doesn't exist: {fnf}")

    else:
        full_text = fin.read()
        print(full_text[:10])

    finally:
        print(f"you just looked at a file named {book}")








#
# try:
#     with open('wa_and_peace.txt', 'r') as fin:
#         full_text = fin.read()
# except FileNotFoundError as fnf:
#     print("file name misspelled! double-check!")
# except ValueError:
#     print("oh no")
# else:
#     print(full_text[:1000])
# finally:
#     print("keep reading!")
