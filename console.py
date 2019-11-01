# populate a list from console 
# exit when users says 'quit'

lst = []
while ((console_input := input("Say something: ")) != 'quit'):
    lst.append(console_input)
print('You entered : ')

string = str()
for item in lst:
    #string = string + item + ' '
    output = ' '.join(l for l in lst)
print(output)
"""
lst = []
while (current := input("Write something: ")) != "quit":
    lst.append(current)

"""