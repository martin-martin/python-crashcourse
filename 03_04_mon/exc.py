try:
    with open('wa_and_peace.txt', 'r') as fin:
        full_text = fin.read()
except FileNotFoundError as fnf:
    print("file name misspelled! double-check!")
else:
    print(full_text[:1000])
finally:
    print("keep reading!")
