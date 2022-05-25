import random, time

print(random.randint(0, 1))

cardset = input('Enter the file name of you flashcards, e.g. "Cards.txt" \n')

cards = open(cardset)
read = cards.readlines()
QnO = read[0]

if QnO.isnumeric() == True:    
    revise = True
    while revise == True:
        askme = random.randint(1, int(QnO)) * 3
        askme = askme - 2
        print("-------------------------------------------------------------------------")
        print(read[askme])
        answer = input('Answer: ("Type "Q" to end the program) \n')
        if answer.upper() == "Q":
            cards.close()
            revise = False
            quit()
        print()
        print(read[askme + 1])
        time.sleep(1)
else:
    QnO = input("How many cards are in the file? \n")
    revise = True
    while revise == True:
        askme = random.randint(1, int(QnO)) * 3
        askme = askme - 3
        print("-------------------------------------------------------------------------")
        print(read[askme])
        answer = input('Answer: ("Type "Q" to end the program) \n')
        if answer.upper() == "Q":
            cards.close()
            revise = False
            quit()
        print()
        print(read[askme + 1])
        time.sleep(1)
