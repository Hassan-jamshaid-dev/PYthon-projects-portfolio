# ROCK<PAPER<SCISSOR GAME





import random
options = ("rock","paper","scissor")
player =None
computer = random.choice(options)

while player not in options:
       player = input("Enter either of the three (rock,paper or scissor): ").lower()

print(f"Computer: {computer}")
print(f"Player: {player}")

if computer == player:
       print("TIE!")
elif computer == "rock" and player == "paper":
       print("YOU WIN!")
elif computer == "scissor" and player == "rock":
       print("YOU WIN!")
elif computer == "paper " and player == "scissor":
       print("YOU WIN!")
else:
       print("YOU LOSE!")