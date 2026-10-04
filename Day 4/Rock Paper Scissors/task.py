import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: '))
if choice == 0:
    player_choice = rock

elif choice == 1:
    player_choice = paper

elif choice == 2:
    player_choice = scissors
else:
    print("Invalid Choice")



computer_choice = random.choice(rps)
print(f'You chose {player_choice}')
print(f'Computer chose {computer_choice}')
if player_choice == computer_choice:
    print('Its a tie!')
elif ((player_choice == rock and computer_choice == scissors)
        or (player_choice == scissors and computer_choice == paper)
        or (player_choice == paper and computer_choice == rock)):
    print ('You win!')
else:
    print ('You lose!')
