def mid(word):
    found = ""
    if len(word) % 2 == 0:
        return found
    else:
        index = len(word)/2 + 0.5 - 1
        return word[int(index)]