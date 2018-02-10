#  File: Poker.py

#  Description:

#  Student's Name:

#  Student's UT EID:

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)

    # determine the each type of hand and print
    points_hand = []  # create list to store points for each hand

    for i in range (len(self.players)):
      if is_royal(self.players[i]) != 0:
        points_hand.append(is_royal(self.players[i]))
        print("Player", str(i + 1)+ ": Royal Flush")
      elif is_straight_flush(self.players[i]) != 0:
        points_hand.append(is_straight_flush(self.players[i]))
        print("Player", str(i + 1)+ ": Straight Flush")
      elif is_four_kind(self.players[i]) != 0:
        points_hand.append(is_four_kind(self.players[i]))
        print("Player", str(i + 1)+ ": Four of a Kind")
      elif is_full_house(self.players[i]) != 0:
        points_hand.append(is_full_house(self.players[i]))
        print("Player", str(i + 1)+ ": Full House")
      elif is_flush(self.players[i]) != 0:
        points_hand.append(is_flush(self.players[i]))
        print("Player", str(i + 1)+ ": Flush")
      elif is_straight(self.players[i]) != 0:
        points_hand.append(is_straight(self.players[i]))
        print("Player", str(i + 1)+ ": Straight")
      elif is_three_kind(self.players[i]) != 0:
        points_hand.append(is_three_kind(self.players[i]))
        print("Player", str(i + 1)+ ": Three of a Kind")
      elif is_two_pair(self.players[i]) != 0:
        points_hand.append(is_two_pair(self.players[i]))
        print("Player", str(i + 1)+ ": Two Pair")
      else:
        points_hand.append(is_high_card(self.players[i]))
        print("Player", str(i + 1)+ ": High Card")
    # determine winner and print
    max_players = [] # list of players with max total points value
    max_val = max(points_hand)
    for i in range len(points_hand):
      if points_hand[i] == max_val:
        max_players.append(i+1)
    if len(max_players) == 1:
      print("Player", str(max_players[0]), "wins.")
    else:
      for i in len(max_players):
        print("Player", str(max_players[i], "ties."))


  # determine if a hand is a royal flush
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)
    
    return (same_suit and rank_order)

 
  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False
    
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and ((hand[i].rank + 1) == hand[i + 1].rank)
    
    return (same_suit and rank_order)

  def is_four_kind (self, hand):
    rank_check = hand[0].rank
    for card in hand:
      if card.rank != rank_check:
        return False
    return True

  def is_full_house (self, hand):
    similar_cards_left = 1 #how many cards have similar rank from left
    similar_cards_right = 1 #how many cards have similar rank from the right
    leng = len(hand)
    for i in leng:
      if hand[0].rank == hand[i].rank:
      	similar_cards_left += 1
      if hand[leng-1].rank == hand[leng-i].rank:
        similar_cards_right += 1

    return (if similar_cards_left + similar_cards_right == 5)

  def is_flush (self, hand):
    for i in range (len(hand) - 1):
      if hand[i].suit != hand[i + 1].suit:
        return False
    return True

  def is_straight (self, hand):
    ...

  def is_three_kind (self, hand):
    ...

  def is_two_pair (self, hand):
    ...

  '''
  # determine if a hand is one pair
  def is_one_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return True
    return False

  '''
  def is_high_card (self, hand):
    ...

def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)

  # play the game (poker)
  game.play()

main()

'''

#Royal Flush
suit_check = hand[0].suit
total_rank = 14 + 13 + 12 + 11 + 10 #when suit is same, rank_check = total_rank only if royal flush
rank_check = 0
for card in hand:
  if card.suit != suit_check:
    return False
  rank_check += card.rank
if rank_check != total_rank:
  return False
return True

#Straight Flush


#Four of a Kind
rank_check = hand[0].rank
for card in hand:
  if card.rank != rank_check:
    return False
return True

#Full House (this code is janky)
similar_cards = 0 #how many cards have similar rank
rank_check = hand[0].rank
for card in hand:
  if rank_check == card.rank:
    similar_cards += 1
return if similar_cards == 3 or similar_cards == 2

#Flush
suit_check = hand[0].suit
for card in hand:
  if suit_check != card.suit:
    return False
return True

#Straight


