from fighters import Fighters
import random


def file_characters(filename):
    '''
    read file and creates a list of plable characters in a list
    '''
    
    f = open(filename, 'r') 
    
    #f.readline() later when i redo the txt
    
    charactersList = []
    
    for aline in f:
        alinelist = aline.strip().split(',')
        acharacter = Fighters() 
        acharacter.setName(alinelist[0])
        acharacter.setHpBar(alinelist[1])
        acharacter.setSuper(alinelist[2])
        acharacter.setRoll1(alinelist[3])
        acharacter.setBasic(alinelist[4])
        acharacter.setRoll2(alinelist[5])

        charactersList.append(acharacter)
        
    return charactersList


def instructions():
    '''
    Displays the game rules
    '''
    print("\nThis is a two-player game. Each player picks a character.")
    print("Each character has certain super attacks and basic attacks with different roll costs.")
    print("Players take turn attacking and must roll the cost amount or higher to initiate attack.")
    print("A winner is declared once a player drops the opposing player character hp to 0.")


def character_choice(characters):
    '''
    prompt the user to choose any of the avaliable characters
    returns the number for set character
    '''
    print("Character number 0")
    print(characters[0])
    print("\nCharacter number 1")
    print(characters[1])
    print("\nCharacter number 2")
    print(characters[2])
    print("\nCharacter number 3")
    print(characters[3])
    print("\n")
    
    player1_choose = int(input("Player 1: Enter the character number of your choosing: "))
    
    while True:
        if player1_choose == 0:
            player1 = player1_choose
            break
        elif player1_choose == 1:
            player1 = player1_choose
            break
        elif player1_choose == 2:
            player1 = player1_choose
            break
        elif player1_choose == 3:
            player1 = player1_choose
            break
        else:
            print("Not valid try again")
            player1_choose = int(input("Player 1: Enter the character number of your choosing: "))
    
    player2_choose = int(input("Player 2: Enter the character number of your choosing: "))
    while True:
        if player2_choose == 0:
            player2 = player2_choose
            break
        elif player2_choose == 1:
            player2 = player2_choose
            break
        elif player2_choose == 2:
            player2 = player2_choose
            break
        elif player2_choose == 3:
            player2 = player2_choose
            break
        else:
            print("Not valid try again")
            player2_choose = int(input("Player 2: Enter the character number of your choosing: "))
           
    return (player1, player2)


def player_hp(characters, player):
    '''
    creates a variable for hp to deduct attack from later on
    since list are compromised of different data types
    '''
    hp = 0
    hp = characters[player].getHpBar()
    return hp


def display_fighters(player1, player2, player1_hp, player2_hp, characters):
    '''
    displays the characters hp bar, name, and fighter for both players
    '''
    print("          Fighters          ")
    print("____________________________")
    print(characters[player1].getName(), "                ", characters[player2].getName()) 
    print("Hp: ", player1_hp, "             ", "Hp: ", player2_hp)      
    print("   O                   O" +
          "\n  /|\\                 /|\\" +
          "\n  / \\                 / \\")
          
def startBattle():
    '''
    will prompt the users if they are ready to start to start the battle
    '''
    ans = input("Ready to start? Enter yes or no: ")
    while True:
        if ans.lower() == 'yes':
            return True
        else:
            return False
          
    
def rollDice():
    '''
    Prompts both players to roll 2 dices and the player
    with the highest number will attack first
    I also picked up this dice art from an outside source
    '''
    
    
    dice_art = {
    1: ("[1]"),
    2: ("[2]"),
    3: ("[3]"),
    4: ("[4]"),
    5: ("[5]"),
    6: ("[6]")
}

    dice = []
    dice2 = []

    total1= 0
    total2 = 0
    
    print("\nEach player will roll two dice. The player with the highest sum will attack first")
    checker = True
   
    while total1 == total2:  
        player1 = input("Player 1 hit Enter to roll the dice...")
        if player1 == "":
            for roll in range(2):
                dice.append(random.randint(1, 6))
                print(dice_art[dice[roll]])
        for roll in dice:
            total1 += roll
        print("Total: " + str(total1))

        player2 = input("\nPlayer 2 hit Enter to roll the dice...")
        if player1 == "":
            for roll in range(2):
                dice2.append(random.randint(1, 6))
                print(dice_art[dice2[roll]])
                total2 += roll
        for roll in dice2:
            total2 += roll
        print("Total: " + str(total2)) 
        
        if total1 > total2 or total2 > total1:
            break
        else:
            total1 = 0
            total2 = 0
        
    if total1 > total2:
        return True
    else:
        return False
    

def attack_turn(player, characters):
    '''
    Displays characters moveset and roll cost to use.
    prompts the user to deciede which form of attack they will attack the other player with
    '''
    print("\n" + characters[player].getName() + " Movesets below and Cost")
    print("Super: " + characters[player].getSuper() + 
          "\nRoll cost: " + characters[player].getRoll1())
    print("Basic: " + characters[player].getBasic() + 
          "\nRoll cost: " + characters[player].getRoll2())

    dice_art = {
    1: ("[1]"),
    2: ("[2]"),
    3: ("[3]"),
    4: ("[4]"),
    5: ("[5]"),
    6: ("[6]")
}

    dice = []
    total = 0
    
    print("\nAttacking player will roll 3 dice. If the sum is greater than or equal to the cost it will attack the rolled amount")
    player_choice = int(input("Enter 1 for Super or 0 for basic attack and you will roll: "))
    
    while True:
        if player_choice == 1:
            for roll in range(3):
                dice.append(random.randint(1, 6))
                print(dice_art[dice[roll]])
            for roll in dice:
                total += roll 
            if total >= int(characters[player].getRoll1()):
                print(characters[player].getName() + " attacks with a super for a total of ", total, " damage.") 
                break
            else:
                print(characters[player].getName() + " didn't land the super.")
                total = 0
                break
   
        if player_choice == 0:
            for roll in range(3):
                dice.append(random.randint(1, 6))
                print(dice_art[dice[roll]])
            for roll in dice:
                total += roll
        
            if total >= int(characters[player].getRoll2()):
                print(characters[player].getName() + " uses basic attack for a total of ", total, " damage.") 
                break
            else:
                print(characters[player].getName() + " didn't land the attack.")
                total = 0
                break 
        else:
            print("\nNot a valid number, try again.")
            player_choice = int(input("Enter 1 for Super or 0 for basic attack and you will roll: "))
        
    return total
            
                
def winner(player, characters, player_chara):
    '''
    Displays the winners name and the character they used
    '''
    
    print("\n**********Congratulations to", player, "for becoming victorious as", characters[player_chara].getName(), "you are the champion!************")
    

def replay():
    '''
    prompts the user if they would want to continue playing or exit the game
    '''

    again = input("\nWould you like to play again? Yes or no? ")
    while True:
        if again.lower() == "yes":
            return True
        else:
            return False

    
def startGame(characters):
    '''
    The main controller
    '''
    print(">>> Welcome to my Beta DND Battle! <<<")
    instructions()
    # will be added later
    print("\n")
    
    while True:
        
        player1_chara, player2_chara = character_choice(characters) #tuple
        print("\nPlayer 1 has chosen " + characters[player1_chara].getName() +
              "\nPlayer 2 has chosen " + characters[player2_chara].getName())
        print("\n")
        
        player1_hp = player_hp(characters, player1_chara) 
        player2_hp = player_hp(characters, player2_chara) 
    
    
        display_fighters(player1_chara, player2_chara, player1_hp, player2_hp, characters)
            
        turn = rollDice() 
        
        readyOrNot = startBattle()

    #------------------------------------player 1------------------------------------------------
        while readyOrNot: # one player wins
            if turn == True:
                print("\nPlayer 1 will attack")   
                attack = attack_turn(player1_chara, characters)
                player2_hp = int(player2_hp) - int(attack)
                if player2_hp > 0:
                    print("\nSwitching turns!")
                    print("\n")
                    display_fighters(player1_chara, player2_chara, player1_hp, player2_hp, characters)
                    turn = False 
                elif player2_hp <= 0:
                    winner("player 1", characters, player1_chara)
                    readyOrNot = False
     #------------------------------------Player 2--------------------------------------------------          
            if turn == False:
                print("\nPlayer 2 will attack")   
                attack = attack_turn(player2_chara, characters)
                player1_hp = int(player1_hp) - int(attack)
                if player1_hp > 0:
                    print("\nSwitching turns!")
                    print("\n")
                    display_fighters(player1_chara, player2_chara, player1_hp, player2_hp, characters)
                    turn = True
                elif player1_hp <= 0:
                    winner("player 2", characters, player2_chara)
                    readyOrNot = False
      #---------------------Exit----------------------
        display_fighters(player1_chara, player2_chara, player1_hp, player2_hp, characters)
        if not replay():
            print("\nThanks for playing my Beta game. :) Goodbye!")
            break
        print("\n")
    
    
    
def main():
    
    file = "characters.txt"
    characters = file_characters(file)
    startGame(characters)
        



if __name__ == "__main__":
    main()