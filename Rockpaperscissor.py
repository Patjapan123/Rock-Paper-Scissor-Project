import random

print("Rock Paper Scissor!!!")
print("Enter your choice")
userpick=input()
print("Now it is the computer turn")
print("The computer choose")
cpu=["Rock","Paper","Scissor"]
computerpick=random.choice(cpu)
print(computerpick)
while computerpick == userpick:
    print("It is a tie")
    print("pick again")
    userpick=input()
    print("Computer's Turn")
    print(computerpick)
if userpick == "Scissor" and computerpick == "Rock":
    print("You lose. Better luck next time")
if userpick == "Scissor" and computerpick == "Paper":
    print("Great Job. You won!!!")
if userpick == "Paper" and computerpick == "Scissor":
    print("You lose. Better luck next time")
if userpick == "Paper" and computerpick == "Rock":
    print("Great Job. You won!!!")
if userpick == "Rock" and computerpick == "Paper":
    print("You lose. Better luck next time")
if userpick == "Rock" and computerpick == "Scissor":
    print("Great Job. You won!!!")