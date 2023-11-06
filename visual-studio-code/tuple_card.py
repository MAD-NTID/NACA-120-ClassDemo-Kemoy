# A card is made up of Rank,Suit,Color
card = ("Ace", "Heart", "Red")

print(card)
print("The rank is:", card[0])
print("The suit is:", card[1])
print("The color is:", card[2])

# attempt to update the rank
#card[0] = "Jack" oops, we cant change...IMMUTABLE
print(card)

card_two = tuple(("Jack", "Spade", "Black"))

print(type(card))
print(type(card_two))

crazy = (("Ragde", 4.0),("Brian", 4.0))
print(crazy)

lst = [card, card_two]

print(lst)

print("Jack" in card_two)
print("Spade" in card_two)
print(len(card_two))