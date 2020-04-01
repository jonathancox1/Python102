
#prompt user to input a number to represent degrees celsius
c = int(input('Enter a temperature in Celcius to be converted to Farenheit '))

#convert celsius to fahrenheit and save to variable f
f = (c * 1.8) + 32

#return the original temp in celsius as well as converted to fahrenheit
#extra blank prints simply for formatting
print()
print()
print(f'''You gave me {c} degrees Celsius
I give you {f} degrees Fahrenheit''')
print()
print()