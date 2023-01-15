# Chatbot is a software programmed to interact with humans, using Natural Language Processing (NLP)

# Install Chatterbot Python Library
# Documentation: https://chatterbot.readthedocs.io/en/stable/tutorial.html
# pip install chatterbot 
# if the above command doesnt work, try installing the actual version or a version below (aacording to stackoverflow)
# pip install chatterbot==1.0.4

# Install a machine readable multilingual dialog corpus modules
# These modules are used to quickly train ChatterBot to respond to various inputs in different languages
# pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# import corpus trainer that helps to train the bot
from chatterbot.trainers import ChatterBotCorpusTrainer
# NLTK is a leading platform for building Python programs to work with human language data
# pip install --user -U nltk
import nltk
nltk.download('punkt')

# Define the bot, create a new instance of a chatbot class
# Pass parameters: name, read_only, logic adapters
# read_only=True disables bots ability to learn; read_only=False enables ability to learn
# logic adapters is a list of adapters used to train the bot
# multiple adapters can be entered
# The BestMatch logic adapter selects a response based on the best known match to a given statement.
# The MathematicalEvaluation logic adapter checks a given statement to see if it contains a mathematical expression that can be evaluated.
# The TimeLogicAdapter identifies statements in which a question about the current time is asked. 


bot = ChatBot(name='Cleo', read_only=True, logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch","chatterbot.logic.TimeLogicAdapter" ])
#bot = ChatBot('Cleo')

# Define the list of responses
small_talk = ['hi there!',
          'hi!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m Cleo. Ask me a math question, please.']
math_talk_1 = ['pythagorean theorem',
          'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
          'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']


# create and train the bot by creating an instance of ListTrainer and supplying it with the lists of strings
list_trainer = ListTrainer(bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)

# The bot should now be trained and ready to communicate

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

print(bot.get_response("hello"))
# If there's an issue with print install this: pip install pytz

while True:
    try:
        bot_input = input("You: ")
        bot_response = bot.get_response(bot_input)
        print(f"{bot.name}: {bot_response}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break