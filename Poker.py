#  File: Poker.py

#  Description:

#  Student's Name: Audrey McNay

#  Student's UT EID: alm5735

#  Partner's Name: Juan Zambrano

#  Partner's UT EID: jez346

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created: 2/4/18

#  Date Last Modified: 2/10/18

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
      if self.is_royal(self.players[i]) != 0:
        points_hand.append(self.is_royal(self.players[i]))
        print("Player", str(i + 1)+ ": Royal Flush")
      elif self.is_straight_flush(self.players[i]) != 0:
        points_hand.append(self.is_straight_flush(self.players[i]))
        print("Player", str(i + 1)+ ": Straight Flush")
      elif self.is_four_kind(self.players[i]) != 0:
        points_hand.append(self.is_four_kind(self.players[i]))
        print("Player", str(i + 1)+ ": Four of a Kind")
      elif self.is_full_house(self.players[i]) != 0:
        points_hand.append(self.is_full_house(self.players[i]))
        print("Player", str(i + 1)+ ": Full House")
      elif self.is_flush(self.players[i]) != 0:
        points_hand.append(self.is_flush(self.players[i]))
        print("Player", str(i + 1)+ ": Flush")
      elif self.is_straight(self.players[i]) != 0:
        points_hand.append(self.is_straight(self.players[i]))
        print("Player", str(i + 1)+ ": Straight")
      elif self.is_three_kind(self.players[i]) != 0:
        points_hand.append(self.is_three_kind(self.players[i]))
        print("Player", str(i + 1)+ ": Three of a Kind")
      elif self.is_two_pair(self.players[i]) != 0:
        points_hand.append(self.is_two_pair(self.players[i]))
        print("Player", str(i + 1)+ ": Two Pair")
      elif self.is_one_pair(self.players[i]) != 0:
        points_hand.append(self.is_one_pair(self.players[i]))
        print("Player", str(i + 1)+ ": One Pair")
      else:
        points_hand.append(self.is_high_card(self.players[i]))
        print("Player", str(i + 1)+ ": High Card")
    # determine winner and print
    max_players = [] # list of players with max total points value
    max_val = max(points_hand)
    for i in range (len(points_hand)):
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

    if rank_order:
      return 10 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
    else:
      return 0

 
  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False
    
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and ((hand[i].rank + 1) == hand[i + 1].rank)
    
    if rank_order:
      return 9 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
    else:
      return 0

  def is_four_kind (self, hand):
    count = 0
    for card in range(len(hand) - 1):
        if(hand[card].rank == hand[card+1].rank):
            count +=1
            same_card = hand[card].rank
        else:
            different_card = hand[card].rank
    if(count == 4):
        return 8 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
    else:
        return 0

  def is_full_house (self, hand):
    similar_cards_left = 0 #how many cards have similar rank from left
    similar_cards_right = 0 #how many cards have similar rank from the right
    leng = len(hand)
    for i in range (leng-1):
      if hand[0].rank == hand[i].rank:
      	similar_cards_left += 1
      else:
        continue
      if hand[leng-1].rank == hand[leng-i-1].rank:
        similar_cards_right += 1
      else:
        continue

    if (similar_cards_left + similar_cards_right == 5):
      return 7 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
    else: 
      return 0

  def is_flush (self, hand):
    for i in range (len(hand) - 1):
      if hand[i].suit != hand[i + 1].suit:
        return False
    return True

  def is_straight (self, hand):
    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank + 1 == hand[i+1].rank)
    if rank_order:
        return 5 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
    else:
        return 0

  def is_three_kind (self, hand):
    for i in range(len(hand) - 1):
      if hand[i].rank == hand[i+1].rank:
        if (i+2 < len(hand) - 1) and (hand[i+1].rank == hand[i+2].rank):
          return 3 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
      else:
        continue
    return 0

  def is_two_pair (self, hand):
    amount_ranks = []
    for i in range(len(hand)):
      if hand[i].rank not in amount_ranks:
        amount_ranks.append(hand[i].rank)
      else:
        continue
    if len(amount_ranks) != 3:
      return 0
    else:
      return 3 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
 
  def is_one_pair (self, hand):
    amount_ranks = []
    for i in range(len(hand)):
      if hand[i].rank not in amount_ranks:
        amount_ranks.append(hand[i].rank)
      else:
        continue
    if len(amount_ranks) != 4:
      return 0
    else:
      return 2 * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank
 
  def is_high_card (self, hand):
    return 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank

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


