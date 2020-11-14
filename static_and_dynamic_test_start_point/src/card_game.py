### Testing task 2 code:

# Carry out dynamic testing on the code below.
# Correct the errors below that you spotted in task 1.

class CardGame:


  def checkforace(self, card):                    # change 'A' for 'a'
    if card.value == 1:                           # add '='
      return True                                 # replace 't' by 'T'
    else:                                         # add ':'
      return False                                # replace 'f' by 'F'

  
  def highest_card(self, card1, card2):           # replace 'dif' by 'def', add ',', add ':'
    if card1.value > card2.value:                 # add ':'
      return card1                                # add '1' to 'card'
    else:                                         # add ':'
      return card2
 

  def cards_total(self, cards):                    # add 'self'
    total = 0                                      # add '= 0'
    for card in cards:
      total += card.value
    return "You have a total of " + str(total)     # 'str' total, add '' after 'of'

