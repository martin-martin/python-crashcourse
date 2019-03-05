def is_palindrome(text):
    if text == '':
        return False
    if len(text) == 1:
        return False
    if text.isspace():
        return False
    if text == text[::-1]:
        return True
    else:
        return False


def starts_with(word, character):
    if word[0].lower() == character.lower():
        return True
    else:
        return False


def count_characters(word):
    count = 0
    for c in word:
        count += 1
    return count


if __name__ == '__main__':
    print("123")
