# bill_splitter is a program that splits the bill amount somewhat among friends.
# The program keeps the fun alive and makes sure that everyone pays an equal amount. 

import random

num_of_friends = int(input("Enter the number of friends joining (including you):\n"))
print()
friends_dictionary = {}

# nothing to do if there is no friend
if num_of_friends <= 0:
    print("No one is joining for the party")
else:

    # create a dictionary of friends
    print("Enter the name of every friend (including you), each on a new line: ")
    for i in range(num_of_friends):
        name = input()
        friends_dictionary.update({name: 0})
    bill = int(input("\nEnter the total bill:\n"))

    # lucky player chosen pays zero while everyone else pays an equal amount
    choice = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if choice == 'Yes':
        for i in friends_dictionary:
            friends_dictionary[i] = round((bill / (num_of_friends - 1)), 2)
        friends_list = list(friends_dictionary.keys())
        lucky_friend = random.choice(friends_list)
        friends_dictionary[lucky_friend] = 0
        print("\n{} is the lucky one! \n\n{}".format(lucky_friend, friends_dictionary))
    else:
        for i in friends_dictionary:
            friends_dictionary[i] = round((bill / num_of_friends), 2)
        print("\nNo one is going to be lucky\n{}".format(friends_dictionary))
