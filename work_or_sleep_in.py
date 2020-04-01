#prompt user for a number 0-6 to be converted to a day of the week
day = int(input('Enter a day as a number (0-6) and Ill tell you the day of the week '))

#create a default prompt
prompt = 'Your chosen day is:'

#determin the numerical value of the day from the user input
if day == 6 or day == 0:
    print('Go back to bed')
else:
    print('You better get up!!')