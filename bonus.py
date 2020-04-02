#prompt user for input (pets name, street you grew up on, an adjecitive)
user_input = input('Give me an adjective ') + ' '
user_input += input('Give me the street you grew up on ') + ' '
user_input += input('Give me your dogs first name ') + '!'

#print users input
print(f'Hello, {user_input}')

# #another method
# a = input('Give me an adj: '), input('Give me a steet name: '), input('Give me a dogs name: ')

# print(f'Hello, {a[0]}, {a[1]}, {a[2]}')