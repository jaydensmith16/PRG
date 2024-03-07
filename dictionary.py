# Nato dictionary define
dictionary = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India","J": "Juliette", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"}

def spell_word():
    user_word = input("Enter a word:")
    user_word = user_word.upper()
    
for letter in user_word:
    print(dictionary.get(letter))
def main():
    spell_word()

main()