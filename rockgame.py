import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
user = input("enter rock,paper,or scissors:").lower()

if user ==computer:
    print("tie")
elif (user == "rock" and computer == "scissors") or (user == "paper" and  computer == "rock") or (user =="scissors" and computer == "paper"):
    print("You won woho mubarakho")
else:
    print("computer win afsossss")
