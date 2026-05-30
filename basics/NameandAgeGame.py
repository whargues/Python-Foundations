#This program says hello and asks for a name and age

print('Hello')

print('What is your name?') # Asks for name
My_Name=input()
print(f'It is good to meet you {My_Name}!')
print(f'The length of your name is: {len(My_Name)} characters') # Formatted string that displays length of name

print(f'How old are you {My_Name}?') # Asks for age
My_Age=input()
print(f'You are going to be {int(My_Age) + 1} years old next year {My_Name}!!!') # Formatted string that displays age of user next year