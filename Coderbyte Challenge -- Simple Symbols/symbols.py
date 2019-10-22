def SimpleSymbols(str):
    for i in range(len(str)):
        if str[i].isalpha():
            if (i == 0) or (str[i - 1] != "+") or (str[i + 1] != "+"):
                return False
            else:
                return True

print(SimpleSymbols("+f++d+"))
