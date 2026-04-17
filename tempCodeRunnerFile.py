running_total = 0

num_of_friends = input('Input your number of person:')

appetizers = int(input('Input your appetizers prize:'))
main_courses = int(input('Input your main_courese prize:'))
desserts = int(input('Input your dessert prize:'))
drinks = int(input('Input your drink prize:'))

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill,2)
print (f'Each person pays: {each_pays}')