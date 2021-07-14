import itertools

suits = ["C", "H", "S", "D"]
suit_images = [
    "clubbing",
    "pulling from the heart",
    "digging up",
    "wearing on a bracelet",
]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
value_images = [
    "Ace Ventura",
    "R2D2",
    "Scary Tree",
    "Ford Truck",
    "Jackson Five",
    "Caprica Six",
    "Seven Dwarves",
    "Fat Lady",
    "Hitler",
    "Tennis Player",
    "Jack Sparrow",
    "Queen Elizabeth",
    "Elvis",
]
# x = zip(values, value_images)
# y = zip(suits, suit_images)
# deck = itertools.product(values, suits)
# for card in deck:
#     print(f"{card[0]}\t{card[1]}")

for sn, s in enumerate(suits):
    for vn, v in enumerate(values):
        print(f"{v}\t{s}\t{value_images[vn]}\t{suit_images[sn]}")
