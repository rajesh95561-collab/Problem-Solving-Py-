# WAP on string to check string is palindrome or not

def palindrome(string):
    if len(string) <= 1:
        print("the string is palindrome")
    else:
        if string[0] == string[-1]:
            palindrome(string[1:-1])
        else:
            print("the string is not palindrome")


palindrome("mam")
