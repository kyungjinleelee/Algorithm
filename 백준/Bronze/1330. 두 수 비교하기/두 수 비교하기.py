a, b = map(int, input().split())

def compare():
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('==')

compare()