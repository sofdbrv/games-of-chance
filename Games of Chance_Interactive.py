import random
import itertools as it
import sys


money = 100

#### Main playing function ############################

def playing_a_game():
    if money <= 0:
        out_of_money()
    
    chosen_game = input(f'\n--------------------\nYou have got £{money}. \n\nEnter the number of your chosen game: \n(1) Heads or Tails: Pick heads or tails; you win if the coin lands as you predicted. \n(2) Cho Han: Pick odd or even; you win if the sum of two dice is as you predicted. \n(3) Card-Off: You win if the card you pick from a 52-card deck is higher than your opponent\'s. \n(4) Roulette: Pick red/black, odd/even, or a number; you win if the roulette ball lands as you predicted. \nYou choose: ')
    
    if chosen_game.lower() == "no":
        sys.exit()
    if try_int(chosen_game) == False:
        print(f'\nThis value is not accepted. Please enter a number from 1 to 4.')
        playing_a_game()
    elif int(chosen_game) == 1:
        heads_or_tails()
    elif int(chosen_game) == 2:
        cho_han()
    elif int(chosen_game) == 3:
        card_off()
    elif int(chosen_game) == 4:
        roulette()
    else:
        print(f'\nThis value is not accepted. Please enter a number from 1 to 4.')
        playing_a_game()

#### Heads or Tails ############################

def heads_or_tails():
    global money
    all_in = False

    if money <= 0:
        out_of_money()
    
    bet = input(f'\nWelcome to the game of Heads or Tails. \nYou currently have £{money}; please place your bet. \nThe bet must be more than 0 and rounded up to nearest pound. \nYou bet: £')
    if bet.lower() == "no":
        playing_a_game()
    elif bet.isdigit() == False or int(bet) == 0:
        print(f'\nYour bet has not been accepted.')
        heads_or_tails()
    elif money > 0 and money - int(bet) < 0:
        print(f'\nPut a smaller bet on; you don\'t have enough money for this one.')
        heads_or_tails()
    else:
        bet = int(bet)
        if bet == money:
            print("\nYou have gone all in!")
            all_in = True
        
        players_guess = input(f'\nPlease choose Heads (H) or Tails (T): ')
        if players_guess.lower() == "h" or players_guess.lower() == "t":
            players_guess = players_guess.lower()
        elif players_guess.lower() == "heads":
            players_guess = "h"
        elif players_guess.lower() == "tails":
            players_guess = "t"
        players_values = {1: "h", 2: "t"}
        coin_values = {1: "heads", 2: "tails"}
        coin_flip = random.randint(1, 2)
        
        if players_guess.lower() == "no":
            playing_a_game()
        elif not players_guess in players_values.values():
            print(f'\nYour guess is not one of the accepted values. You have lost £{bet}.')
            money -= bet
            if money <= 0:
                out_of_money()
            
            another_game = input(f'\nPlay another game of Heads or Tails? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() == "yes":
                heads_or_tails()
            else:
                playing_a_game()
        
        elif players_values[coin_flip] == players_guess:
            print(f'\nYou chose {coin_values[key_by_value(players_values, players_guess)]}. The coin\'s landed with {coin_values[coin_flip]} up.')
            money += bet

            if all_in == True:
                print(f'You have doubled your money! You now have £{money}.')
            else:
                print(f'You have won £{bet}! You now have £{money}.')
            
            another_game = input(f'\nPlay another game of Heads or Tails? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() =="yes":
                heads_or_tails()
            else:
                playing_a_game()
        
        else:
            print(f'\nYou chose {coin_values[key_by_value(players_values, players_guess)]}. The coin\'s landed with {coin_values[coin_flip]} up.')
            money -= bet
            print(f'You have lost £{bet}. You now have £{money}.')

            if money <= 0:
                out_of_money()
            
            another_game = input(f'\nPlay another game of Heads or Tails? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() =="yes":
                heads_or_tails()
            else:
                playing_a_game()

#### Cho Han ############################

def cho_han():
    global money
    all_in = False

    if money <= 0:
        out_of_money()
    
    bet = input(f'\nWelcome to the game of Cho Han. \nYou currently have £{money}; please place your bet. \nThe bet must be more than 0 and rounded up to nearest pound. \nYou bet: £')
    if bet.lower() == "no":
        playing_a_game()
    elif bet.isdigit() == False or int(bet) == 0:
        print(f'\nYour bet has not been accepted.')
        cho_han()
    elif money > 0 and money - int(bet) < 0:
        print(f'\nPut a smaller bet on; you don\'t have enough money for this one.')
        cho_han()
    else:
        bet = int(bet)
        if bet == money:
            print("\nYou have gone all in!")
            all_in = True
        
        players_guess = input(f'\nPlease choose odd (1) or even (2): ')
        if players_guess.lower() == "odd" or players_guess.lower() == "od" or players_guess.lower() == "o":
            players_guess = 1
        elif players_guess.lower() == "even" or players_guess.lower() == "ev" or players_guess.lower() == "e":
            players_guess = 2
        
        guess_values = {1: "odd", 2: "even"}
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        if players_guess.lower() == "no":
            playing_a_game()
        elif try_int(players_guess) == False:
            print(f'\nYour guess is not one of the accepted values. You have lost £{bet}.')
            money -= bet
            if money <= 0:
                out_of_money()
            
            another_game = input(f'\nPlay another game of Cho Han? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() =="yes":
                cho_han()
            else:
                playing_a_game()
        
        elif not int(players_guess) in range(1, 3):
            print(f'\nYour guess is not one of the accepted values. You have lost £{bet}.')
            money -= bet
            if money <= 0:
                out_of_money()
            
            another_game = input(f'\nPlay another game of Cho Han? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() =="yes":
                cho_han()
            else:
                playing_a_game()
        
        elif (die1 + die2) % 2 == int(players_guess) or (die1 + die2) % 2 == int(players_guess) - 2:
            print(f'\nYou chose {guess_values[int(players_guess)]}. The values of dice were {die1} and {die2}, summing up to {die1 + die2} ({guess_values[int(players_guess)]}).')
            money += bet
            
            if all_in == True:
                print(f'You have doubled your money! You now have £{money}.')
            else:
                print(f'You have won £{bet}! You now have £{money}.')
            
            another_game = input(f'\nPlay another game of Cho Han? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() =="yes":
                cho_han()
            else:
                playing_a_game()
        
        else:
            players_guess = int(players_guess)
            if players_guess == 1:
                outcome = 2
            elif players_guess == 2:
                outcome = 1
            
            print(f'\nYou chose {guess_values[players_guess]}. The values of dice were {die1} and {die2}, summing up to {die1 + die2} ({guess_values[outcome]}).')
            money -= bet
            print(f'You have lost £{bet}. You now have £{money}.')
            if money <= 0:
                out_of_money()
            
            another_game = input(f'\nPlay another game of Cho Han? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() =="yes":
                cho_han()
            else:
                playing_a_game()

#### Card-Off ############################

card_deck = []


def refill_card_deck(i = 1):
    while i < 5:
        for card in range(1, 14):
            card_deck.append(card)
        i += 1


def card_off():
    global money

    all_in = False
    if money <= 0:
        out_of_money()
    
    bet = input(f'\nWelcome to the game of Card-Off. \nYou currently have £{money}; please place your bet. \nThe bet must be more than 0 and rounded up to nearest pound. \nYou bet: £')
    if bet.lower() == "no":
        playing_a_game()
    elif bet.isdigit() == False or int(bet) == 0:
        print(f'\nYour bet has not been accepted.')
        card_off()
    elif money > 0 and money - int(bet) < 0:
        print(f'\nPut a smaller bet on; you don\'t have enough money for this one.')
        card_off()
    else:
        bet = int(bet)
        if bet == money:
            print("\nYou have gone all in!")
            all_in = True
        
        if len(card_deck) <= 1:
            refill_card_deck()
            print("\nYou ran out of cards. The deck has been reshuffled and refilled.")
        
        card_deck_values = {1: "an ace", 2: "a 2", 3: "a 3", 4: "a 4", 5: "a 5", 6: "a 6", 7: "a 7", 8: "an 8", 9: "a 9", 10: "a 10", 11: "a jack", 12: "a queen", 13: "a king"}
        
        players_card = random.choice(card_deck)
        card_deck.remove(players_card)
        opponents_card = random.choice(card_deck)
        card_deck.remove(opponents_card)
        if players_card > opponents_card:
            print(f'\nYou picked {card_deck_values[players_card]}. The opponent picked {card_deck_values[opponents_card]}.')
            money += bet
            
            if all_in == True:
                print(f'You have doubled your money! You now have £{money}.')
            else:
                print(f'You have won £{bet}! You now have £{money}.')
            
            another_game = input(f'\nPlay another game of Card-Off? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() =="yes":
                card_off()
            else:
                playing_a_game()
        
        elif players_card < opponents_card:
            print(f'\nYou picked {card_deck_values[players_card]}. The opponent picked {card_deck_values[opponents_card]}.')
            money -= bet

            print(f'You have lost £{bet}. You now have £{money}.')
            if money <= 0:
                out_of_money()
            
            another_game = input(f'\nPlay another game of Card-Off? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() =="yes":
                card_off()
            else:
                playing_a_game()
        
        else:
            print(f'\nBoth you and your opponent picked {card_deck_values[players_card]}. It\'s a tie!')
            print(f'No money changed hands. You still have £{money}.')

            another_game = input(f'\nPlay another game of Card-Off? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() =="yes":
                card_off()
            else:
                playing_a_game()

#### Roulette ############################

roulette_pockets = ["0", "00"]
for pocket in range(1, 37):
    roulette_pockets.append(str(pocket))


red_pockets = []
black_pockets = []
for pocket in it.chain(range(1, 11), range(19, 29)):
    if pocket % 2 == 1:
        red_pockets.append(str(pocket))
    else:
        black_pockets.append(str(pocket))
for pocket in it.chain(range(11, 19), range(29, 37)):
    if pocket % 2 == 0:
        red_pockets.append(str(pocket))
    else:
        black_pockets.append(str(pocket))



def roulette():
    global money
    all_in = False

    if money <= 0:
        out_of_money()
    
    bet = input(f'\nWelcome to the game of Roulette. \nYou currently have £{money}; please place your bet. \nThe bet must be more than 0 and rounded up to nearest pound. \nYou bet: £')
    if bet.lower() == "no":
        playing_a_game()
    elif bet.isdigit() == False or int(bet) == 0:
        print(f'\nYour bet has not been accepted.')
        roulette()
    elif money > 0 and money - int(bet) < 0:
        print("\nPut a smaller bet on; you don\'t have enough money for this one.")
        roulette()
    else:
        bet = int(bet)
        if bet == money:
            print("\nYou have gone all in!")
            all_in = True
        players_guess = input(f'\nPlease choose red (R), black (B), odd (O/OD), even (E/EV), any one number from 1-36, 0 or 00: ')
        rule_guess_values = ["red", "black", "odd", "even"]
        if players_guess.lower() in rule_guess_values:
            players_guess = players_guess.lower()
        elif players_guess.lower() == "r":
            players_guess = "red"
        elif players_guess.lower() == "b":
            players_guess = "black"
        elif players_guess.lower() == "od" or players_guess.lower() == "o":
            players_guess = "odd"
        elif players_guess.lower() == "ev" or players_guess.lower() == "e":
            players_guess = "even"
        
        roulette_outcome = str(random.randint(1, 38))

        if try_int(players_guess) == True:
            players_guess = str(int(players_guess))

        if roulette_outcome in red_pockets:
            roulette_outcome_colour = "red"
        elif roulette_outcome in black_pockets:
            roulette_outcome_colour = "black"
        else:
            roulette_outcome_colour = "green"
        
        if int(roulette_outcome) in range(1, 37):
            roulette_value = roulette_outcome + " (" + roulette_outcome_colour + ")"
        elif roulette_outcome == "37":
            roulette_value = "0 (" + roulette_outcome_colour + ")"
        elif roulette_outcome == "38":
            roulette_value = "00 (" + roulette_outcome_colour + ")"
        
        if players_guess.lower() == "no":
            playing_a_game()
        elif not players_guess in it.chain(rule_guess_values, roulette_pockets):
            print(f'\nYour guess is not one of the accepted values. You have lost £{bet}.')
            money -= bet

            if money <= 0:
                out_of_money()
            
            another_game = input(f'\nPlay another game of Roulette? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() == "yes":
                roulette()
            else:
                playing_a_game()
        
        else:
            if try_int(players_guess) == True:
                if (players_guess == "red" and roulette_outcome in red_pockets) or (players_guess == "black" and roulette_outcome in black_pockets) or (players_guess == "odd" and int(roulette_outcome) in range(1, 37) and int(roulette_outcome) % 2 == 1) or (players_guess == "even" and int(roulette_outcome) in range(1, 37) and int(roulette_outcome) % 2 == 0):
                    print(f'\nYou have bet on {players_guess}. The ball landed on {roulette_outcome}.')
                    money += bet
                
                    if all_in == True:
                        print(f'You have doubled your money! You now have £{money}.')
                    else:
                        print(f'You have won £{bet}! You now have £{money}.')
                
                elif (int(players_guess) == int(roulette_outcome)) or (players_guess == "0" and roulette_outcome == "37") or (players_guess == "00" and roulette_outcome == "38"):
                    print(f'\nYou have bet on {players_guess}. The ball landed on {players_guess}!')
                    money += (35 * bet)

                    if all_in == True:
                        print(f'You have multiplied your fortune 36x! You now have £{money}!')
                    else:
                        print(f'You have won £{35 * bet}! You now have £{money}.')

                else:
                    print(f'\nYou have bet on {players_guess}. The ball landed on {roulette_value}.')
                    money -= bet
                    
                    print(f'You have lost £{bet}. You now have £{money}.')
                    if money <= 0:
                        out_of_money()

            else:
                if (players_guess == "red" and roulette_outcome in red_pockets) or (players_guess == "black" and roulette_outcome in black_pockets) or (players_guess == "odd" and int(roulette_outcome) in range(1, 37) and int(roulette_outcome) % 2 == 1) or (players_guess == "even" and int(roulette_outcome) in range(1, 37) and int(roulette_outcome) % 2 == 0):
                    print(f'\nYou have bet on {players_guess}. The ball landed on {roulette_outcome}.')
                    money += bet
                    
                    if all_in == True:
                        print(f'You have doubled your money! You now have £{money}.')
                    else:
                        print(f'You have won £{bet}! You now have £{money}.')
                
                elif (players_guess == roulette_outcome) or (players_guess == "0" and roulette_outcome == "37") or (players_guess == "00" and roulette_outcome == "38"):
                    print(f'\nYou have bet on {players_guess}. The ball landed on {players_guess}!')
                    money += (35 * bet)

                    if all_in == True:
                        print(f'You have multiplied your fortune 36x! You now have £{money}!')
                    else:
                        print(f'You have won £{35 * bet}! You now have £{money}.')

                else:
                    print(f'\nYou have bet on {players_guess}. The ball landed on {roulette_value}.')
                    money -= bet
                    
                    print(f'You have lost £{bet}. You now have £{money}.')
                    if money <= 0:
                        out_of_money()
            
            another_game = input(f'\nPlay another game of Roulette? (Y/N) ')
            if another_game.lower() == "y" or another_game.lower() == "yes":
                roulette()
            else:
                playing_a_game()

#### Helper functions ############################

def key_by_value(dictionary, search_value):
    k = list(dictionary.keys())[list(dictionary.values()).index(search_value)]
    return k

def try_int(string_value):
    try:
        int(string_value)
        return True
    except ValueError:
        return False

def out_of_money():
    if money == 0:
        print("You have no money left to play with. You have been kicked out!")
    elif money < 0:
        print("You are £" + str(abs(money)) + " in debt. You have been kicked out!")
    sys.exit()

#### Playing the games ############################

print("\n<<< Welcome to Games of Chance! >>>")
refill_card_deck()
playing_a_game()