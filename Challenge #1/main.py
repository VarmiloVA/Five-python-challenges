from math import pi
from multiprocessing.sharedctypes import Value

def radians_grades_convertor(rad):
    grades = rad*180/pi
    return grades

while True:
    radians = input('\nEnter an angle in radians: ')
    try:
        result = radians_grades_convertor(float(radians))
        print(f'Your angle converted into degrees is equal to {result}º')
    except ValueError:
        if radians.lower() == 'exit':
            break
        else:
            print("Couldn't be converted")
            continue
    except KeyboardInterrupt:
        break