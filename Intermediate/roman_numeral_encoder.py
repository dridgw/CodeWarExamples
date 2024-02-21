roman_dict = {
    'I':1,
    'IV':4,
    'V':5,
    'IX':9,
    'X':10,
    'XL':40,
    'L':50,
    'XC':90,
    'C':100,
    'CD':400,
    'D':500,
    'CM':900,
    'M':1000}

def solution(n):
    # TODO convert int to roman string
    #Confirm valid input
    if not isinstance(n,int) or n < 1 or n > 3999:
        return "Invalid input"
    
    result = ""
    
    # Loop through the dictionary of Roman numerals in descending order of value
    for roman, value in reversed(roman_dict.items()):
        while n >= value:
            result += roman
            n -= value
    
    return result

if __name__ == "__main__":
    input= int(input('Please enter a number between 1 - 3999:'))
    print(solution(input))