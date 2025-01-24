# You have 3 lives. I roll the dice. If i roll 6, you win
# If not a 9, you lose 1 life

from random import randint

lives = 3

while lives > 0:
    roll = randint(1,6)
    if roll == 6:
        print("You rolled a 6! You win!")
        break # this exists the while even if lives still > 0
    print(f"You rolled a {roll}! You lose a life")
    lives -= 1
    print(f"Lives left: {lives}")
else: #else from while
    print("You lost!")