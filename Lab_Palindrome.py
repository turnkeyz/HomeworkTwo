##Kyler Telge 1825829
user_input = input()
new_input = user_input.replace(' ', '')
def is_palindrome(new_input):
  if new_input[::1] == new_input[::-1]:
    return True
  else:
    return False

if(is_palindrome(new_input) == True):
    print(user_input, 'is a palindrome')
else:
    print(user_input, 'is not a palindrome')