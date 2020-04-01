day = int(input('Enter a day as a number (0-6) and Ill tell you the day of the week '))

if day == 0:
    print('Sunday')
elif day > 5:
    print('Saturday')
elif day > 4:
    print('Friday')
elif day > 3:
    print('Thursday')
elif day > 2:
    print('Wednesday')
elif day > 1:
    print('Tuesday')
else:
    print('Monday')