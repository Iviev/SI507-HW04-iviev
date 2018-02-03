from random import randrange
import random

def MagicEight():
    myboolean = True
    while myboolean == True:
        question = input("What is your question? To quit, enter 'quit'")

        if question == 'quit':
            break
             # myboolean== False

        elif "?" not in question:
            print("I'm sorry, I can only answer questions.")
            myboolean==False

        else:
            random_words = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
            "Reply hazy, try again", "Ask again later", "Better not tell you know", "Cannot predict now", "concentrate and ask again", "Don’t count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
            magic_random = randrange(0, len(random_words))
            print(random_words[magic_random])

Magic() #invoking the function magic
