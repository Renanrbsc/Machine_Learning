# -*- coding: utf-8 -*-

#----- importing libraries -----#
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#----- Instantiating Chatbot named Lire -----#
bot = ChatBot('Lire')

#----- Defining initial conversation list -----#
conversation = [
    'oi',
    'ola',
    'tudo bem?',
    'tudo e com você',
    'estou bem',
    'que otimo, fico feliz',
    'qual o seu nome?',
    'Lire',
    'prazer em te conhecer',
    'Prazer é meu',
    'o que você é?',
    'sou um bot criado por você!'
]

#----- Instantiating training to the bot -----#
trainer = ListTrainer(bot)

#----- setting conversation to the bot -----#
trainer.train(conversation)

#----- progress looping -----#
while True:
    #----- Defining condition based on degree of confidence -----#
    try:
        response = bot.get_response(input("Você: "))
        if float(response.confidence) > 0.5:
            print("Lire: ", response)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
    