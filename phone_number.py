#write a function that takes in a string
#containing a phone number and presents
#it in the format '234 - 1234 - 5678 - 901'

def phone_number(number : str = "") -> str:

    count = 0
    stack = []
    result = ""
    code = '234 - '


    for i in number:

        count += 1
        stack.append(i)

        if count == 4:
            stack.append(' ')
            stack.append('-')
            stack.append(' ')

        if count == 8:
            stack.append(' ')
            stack.append('-')
            stack.append(" ")

    result = result.join(stack)
    result = code + result

    for x in range(len(stack)):
        stack.pop()

    return result

if __name__=="__main__":
    print(phone_number("08064725214"))

    
