##Kyler Telge 1825829
oldpass = input()
password = ''
for element in oldpass:
    if element == 'i':
        password += '!'
    elif element == 'a':
        password += '@'
    elif element == 'm':
        password += 'M'
    elif element == 'B':
        password += '8'
    elif element == 'o':
        password += '.'
    else:
        password += element

password +='q*s'
print(password)