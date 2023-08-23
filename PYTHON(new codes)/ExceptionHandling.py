try:
    num = int(input('Enter a number: '))
    print(num+2)
except Exception as e:
    print('You have to input a number, ur error is: ', e)