# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)
# # prints 10, not sure why

# b = 300
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b = foobar()
# print(b)

# def nbc(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(nbc(2,3))
# print(nbc(5,3))
# print(nbc(2,3) + nbc(5,3))


# numeral(5)
def tonumeral(num):
    result = ""
    for n in range(0,num):
        if num == 5:
            result = 'V'
        elif num > 9:
            result = 'X'
        elif num > 8:
            result = 'XI'
        elif num > 7:
            result = 'VIII'
        elif num > 6:
            result = 'VII' 
        elif num > 5:
            result = 'V' 
            result += 'I'
        else:
            result += 'I'
    print(result)
    return result

tonumeral(7)


def tonumeral2(num):
    result = ""  # Initialize an empty string to store the Roman numeral
    if num >= 90:
        result += 'XC'  * (num // 90)
        num %= 90
    if num >= 50:
        result += 'L' * (num // 50)
        num %= 50
    # Handle multiples of 10 (e.g., 10, 20, 30, etc.) using 'X'

    if num >= 10:
        result += 'X' * (num // 10)  # Add 'X' repeated as many times as needed
        num %= 10  # Update num to the remainder after handling tens

    # Check for special cases where the numeral should be 'IX' for 9 or 'IV' for 4
    if num == 9:
        result += 'IX'
    elif num >= 5:
        result += 'V'  # Add 'V' for numbers greater than or equal to 5
        num -= 5  # Update num to handle the remainder

    # Handle the remaining 1's
    if num == 4:
        result += 'IV'
    else:
        result += 'I' * num  # Add 'I' repeated as many times as needed

    print(result)  # Print the Roman numeral
    return result

# Example usage:
tonumeral2(7)  # This will print 'VII'


tonumeral2(10)

# def numcon(numeral):
#     I = 0
#     V = 5
#     X = 10
#     L = 50
#     C = 100
#     D = 500
#     M = 1000
#     result = ""
#     for n in numeral:
#         I = I + 1
#         result = I
#         if n == "V":
#             V += 5
#             result = result + V
#     print(result)
#     return result
    
# numcon('VIII')

def numcon(numeral):
    # Define the values of Roman numerals
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0  # Initialize the result to zero

    # Iterate through each character in the input Roman numeral
    for i in range(len(numeral)):
        # Get the value of the current Roman numeral character
        current_value = roman_values[numeral[i]]

        # Check if we need to subtract the previous value
        if i > 0 and current_value > roman_values[numeral[i - 1]]:
            result += current_value - 2 * roman_values[numeral[i - 1]]
        else:
            result += current_value

    print(result)  # Print the Arabic numeral
    return result

# Example usage:
numcon('MVI')  # This will print '8'










