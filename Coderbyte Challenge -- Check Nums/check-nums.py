def CheckNums(num1, num2):
    if num2 > num1:
        returnString = "true"
    elif num1 > num2:
        returnString = "false"
    else:
        returnString = "-1"
    return returnString
