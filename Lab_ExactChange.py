##Kyler Telge 1825829
def exact_change(user_total):
    num = 0
    if (user_total <= 0):
        print('no change')
    dollars = user_total//100
    user_total%=100
    if(dollars>0):
        if (dollars < 2):
            print(dollars, 'dollar')
        else:
            print(dollars, 'dollars')
    quarters= user_total//25
    user_total%=25
    if (quarters > 0):
        if (quarters < 2):
            print(quarters, 'quarter')
        else:
            print(quarters, 'quarters')
    dimes=user_total//10
    user_total%=10
    if (dimes > 0):
        if (dimes < 2):
            print(dimes, 'dime')
        else:
            print(dimes, 'dimes')
    nickels=user_total//5
    user_total%=5
    if (nickels > 0):
        if (nickels < 2):
            print(nickels, 'nickel')
        else:
            print(nickels, 'nickels')
    pennies=user_total
    if (pennies > 0):
        if (pennies < 2):
            print(pennies, 'penny')
        else:
            print(pennies, 'pennies')
    return dollars,quarters,dimes,nickels,pennies

if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

