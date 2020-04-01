#prompt user for a number 0-6 to be converted to a day of the week
day = int(input('Enter a day as a number (0-6) and Ill tell you the day of the week '))

#create a default prompt
prompt = 'Your chosen day is:'

#determin the numerical value of the day from the user input
if day == 0:
    print(f'{prompt} Sunday')
elif day > 5:
    print(f'{prompt} Saturday')
elif day > 4:
    print(f'{prompt} Friday')
elif day > 3:
    print(f'{prompt} Thursday')
elif day > 2:
    print(f'{prompt} Wednesday')
elif day > 1:
    print(f'{prompt} Tuesday')
else:
    print(f'{prompt} Monday')