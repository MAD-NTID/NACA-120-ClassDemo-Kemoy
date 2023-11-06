def make_card_deck():
    cards = []
    ranks = ["Ace", "King","Queen","Jack"]
    suits = ["Diamond", "Club", "Spade", "Heart"]

    #create a rank from 2 - 10
    for i in range(2,11):
        ranks.append(i)
    
    #create a card for every ranks
    for rank in ranks:
        #each rank have a suit
        for suit in suits:
            color = "Black"
            if suit == "Heart" or suit == "Diamond":
                color = "Red"
            #make the card with the appropriate rank, suit and color
            card = (rank,suit,color)
            #add the card to the list
            cards.append(card)
    
    #we created all the cards so we will return it
    return cards

    
    #print(ranks)
def shuffle(deck):
    import random
    for i in range(52):
        first_card_position = random.randint(0,len(deck)-1)
        second_card_position = random.randint(0,len(deck)-1)

        temp = deck[first_card_position]

        deck[first_card_position] = deck[second_card_position]
        deck[second_card_position] = temp
    return deck

def draw_card(deck):
    top_position = len(deck) - 1
    top_card = deck.pop(top_position)

    return top_card

deck = make_card_deck()
deck = shuffle(deck)
while len(deck) > 0:
    card = draw_card(deck)
    print(card)


