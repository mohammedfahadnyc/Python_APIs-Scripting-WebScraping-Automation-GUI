import random
from Art import logo
#from replit import clear
from Art import CARDS, Cards

def deal_cards () :
  cards = [10,10,10,10,9,8,7,6,5,4,3,2,11]
  return random.choice(cards)

def calculate_score (cards_list) :
  if len(cards_list) ==2 and sum(cards_list)==21 :
    return 0
  if 11 in cards_list and sum(cards_list)>21 :
    cards_list.remove(11)
    cards_list.append(1)
  return sum(cards_list)
  
def compare_scores (user_score, computer_score,name) :
  if user_score ==21 and computer_score ==21 :
    return (f"{name} lost\n")
  elif user_score == 0 :
    return (f"{name} won with BlackJack\n")
  elif computer_score ==0  :
    return ("Dealer Won with BlackJack\n")
  elif user_score >  21 :
    return (f"{name} went over. Dealer won\n")
  elif computer_score >21 :
    return ("Dealer went over. You won\n")
  elif computer_score < user_score :
    return (f"{name} won \n")
  else :
      return ("Dealer won \n")
    
def game () :
  name = input("Please Enter Your name . \n")
  user_cards = []
  computer_cards = []
  for i in range (2) :
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
  is_game_end = False

  while is_game_end == False :        #43 to 55
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print (f"Your cards are {user_cards} and your score is {user_score} \n Dealers first card is {computer_cards[0]}\n")
    if user_score == 0 or computer_score == 0 or user_score >21 :
      is_game_end = True
    else :
      if input("Press y to hit, n to stand \n").lower() == "y" :
        user_cards.append(deal_cards())
        #n = Cards.index(user_cards[-1])
        print (f"Your card is {CARDS[Cards.index(user_cards[-1])]}")
        is_game_end = False
      else :
        is_game_end = True

  while computer_score >0 and computer_score <17 :
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)


  print (f"Your final hands are  {user_cards} and your score is {user_score} \n")
  print (f"Dealer's final hands are {computer_cards} and dealer's final score is {computer_score} \n")
  print (compare_scores(user_score, computer_score,name))


while input("Do you want to play a game of BlackJack? y/n \n").lower() == 'y' :
  #clear()
  print (logo)
  game()
