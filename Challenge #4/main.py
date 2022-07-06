def hide(number):
    numbers = []
    for i in number:
        numbers.append(i)

    hiden_number = ''

    for i in range(len(numbers)-4):
        hiden_number += '*'

    for i in range(4):
        hiden_number += f'{numbers[-i]}'

    return hiden_number

print("To stop the program type exit")

while True:
    number = input('\nEnter a credit card number: ')
    try:
        test = int(number)
        hiden_number = hide(number)
        print(f'Your hidden card number is {hiden_number}')

    except ValueError:
        if number.lower() == 'exit':
            break
        else:
            print("Couldn't be hidden")
            continue
    except KeyboardInterrupt:
        break