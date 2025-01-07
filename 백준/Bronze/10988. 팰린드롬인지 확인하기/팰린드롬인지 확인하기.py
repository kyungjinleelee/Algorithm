str = str(input())
reverse_str = str[::-1]

def confirm_palindrom(str, reverse_str):
    if str == reverse_str:
        print(1)
    else:
        print(0)

confirm_palindrom(str, reverse_str)