'''
Author:Jacob Thomas
Date:06/12/2024
Description:Write a program to play a sticks game in which there are 16 sticks. Two players take turns to play the game. Each player picks one set of sticks (needn’t be adjacent) during his turn. A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser. The number of sticks in the set is to be input.
'''
print("Welcome to the Stick Game")
print("Description:The player who pick the stick last loses the game")
print("Rules:")
print("This is a two player game\n Players can take 1,2 or 3 sticks \n 16 sticks are on the table\n A player can take a set of sticks at a time ")
stick=16
player1=input("Enter the name of the first player:" )
player2=input("Enter the name of the second player: ")
n=1
while True:
    turn = player1 if n % 2 != 0 else player2
    print(f"Remaining sticks: {stick}")
    number_of_sticks_in_the_set = int(input(f"{turn}, pick a set of 1,2 or 3 sticks: "))
    if (stick - number_of_sticks_in_the_set) < 0:
        print("\nInsufficient sticks. Please Try Again.")
        continue
    elif stick == number_of_sticks_in_the_set:
        print(f"\n{turn} Lost the game.")
        break
    else:
        stick -= number_of_sticks_in_the_set
    n += 1
