#tip calculator App
food_amount = float(input("enter food amount $:" ))
tip_percentage = float(input("enter your tip percentage %:")) / 100
tip_amount = food_amount * tip_percentage
total = food_amount + tip_amount
print('\n\n\n')
print('--------------------------------')
print(f'food Amount: ${food_amount}')
print(f'tip Amount: ${tip_amount}')
print('\n')
print(f'total amount: ${total}')
print('--------------------------------')
# print(tip_amount)
# print("$" + str(total))