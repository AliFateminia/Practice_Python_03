import random

def prediction():
    words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']
    word = random.choice(words)  # clock
    # print("word: ", word)
    joon = 10
    c = True
    while joon > 0:
        print("joon: ", joon)
        print("The length of the word is", len(word), "letters",'- ' * len(word)) # - - - - -
        print("Enter the word you are guessing >>> ", end=" ")
        user_character = input() # s
        user_character = user_character.lower()
        if user_character in word:
            print("** ** you win ** **")
            c = False
            while c != 1:
                user_character = input("Enter \"yes\" to continue, otherwise enter \"no\" :  ")
                if (c == False) & (user_character == "yes"):
                    c = True
                    prediction()
                if (c == False) & (user_character == "no"):
                    exit()
        else:
            joon = joon - 1
            print('no')
prediction()