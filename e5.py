import random

lower_bound = int(input('Give the lowerbound number: '))
upper_bound = int(input('Give the upperbound number: '))

if lower_bound >= upper_bound:
    print('Notpossible sir')

else:
    random_number = random.randint(lower_bound + 1, upper_bound - 1)
    print(f"Your lower number is {lower_bound} & your upper number is {upper_bound}. The result is {random_number}")