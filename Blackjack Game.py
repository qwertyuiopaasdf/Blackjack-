import random

def deal_card():
	cards= [2,3,4,5,6,7,8,9,10,10,10,10,11]*4
	return random.choice(cards)


def calculate_value(cards):
	return sum(cards)


def compare_values(user_value,dealer_value):
	if user_value>21 and dealer_value>21:
		print("Draw because you both bust")
	elif user_value== dealer_value:
		print ("The game is a draw")
		game_over= True
	elif user_value>dealer_value and user_value<21:
		print("You win")
		game_over= True
	elif user_value<dealer_value and dealer_value<21:
		print ("You loose")
		game_over= True
	elif user_value>21:
		print("You loose because you exceeded 21")
		game_over= True
	elif user_value==21:
		print("You win. Blackjack!")
		game_over= True
	elif dealer_value == 21:
		print("You loose. Dealer has Blackjack!")
		game_over= True
	elif dealer_value> 21:
		print("You win. The dealer exceeded 21")
		game_over= True
	else:
		pass


def play_game():
	print("Lets play Blackjack. Keep hitting until you get to 21, but remember if you axceed 21 you will loose")


	user_cards= [deal_card() for i in range(2)]
	dealer_cards= [deal_card() for i in range (2)]

	game_over= False

	while not game_over: 
		user_value= calculate_value(user_cards)
		dealer_value= calculate_value(dealer_cards)

		print(f"Your cards are {user_cards} and that amounts to {user_value} points")
		print(f"The Dealer's cards are {dealer_cards[0]} and <Second card is hidden>")

		if user_value== 21 or dealer_value==21:
			compare_values(user_value,dealer_value)
			game_over= True
		else:
			x= input("Do you want to hit or stand? Type in 'hit' or 'stand'")
			if x=="hit":
				user_cards.append(deal_card())
				user_value= calculate_value(user_cards)
				if user_value>21:
					
					game_over= True
				
			elif x=="stand":
				print("You stand ")
				compare_values(user_value,dealer_value)
				game_over=True

	while dealer_value != 0 and dealer_value<17:
		dealer_cards.append(deal_card())
		dealer_value= calculate_value(dealer_cards)
		


	print(f"The cards you finally have: {user_cards} and this amounts to {user_value}")
	print(f"The cards the dealer finally has: {dealer_cards} and this amounts to {dealer_value}")
	print(compare_values(user_value,dealer_value))
	if x=="yes":
		play_game()
	if x=="no":
		print("Ok have a good day")
	else:
		print("I am assuming that is a no")

play_game()
