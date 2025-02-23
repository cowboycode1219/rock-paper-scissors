import random

if input():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    #scissors beats paper, rock beats scissors, paper beats rock
    print("Computer picked:", computer_choice)
