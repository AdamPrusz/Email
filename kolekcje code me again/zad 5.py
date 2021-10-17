# utwórz na sztywno 2 wymiarową tablice, tak aby kolejne wiersze zawierały dane osób, natomiast w kolumnach
#bedzie znajdować sie imie nazwisko zawod

celebirities = [
    ["Michał", "Ludek", "student"],
    ["Aleks", "Markiewicz", "prawnik"],
    ["Milena", "Markiewicz", "psycholog"],
    ["Adam", "Pruszyński", "programista"]
]

for person in celebirities:
    print("---".join(person))

