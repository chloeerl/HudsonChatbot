from django.shortcuts import render, redirect
from django.http import HttpResponse

# import libraries for chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

# create an instance of chatbot 
chatbot = ChatBot(
    # name of chatbot
    "Hudson",
    # connect the chatbot to SQL databases
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.responses',
    # determine logic on how chatbot selects a response
    logic_adapters=[
        {
            # selects response based on best known match
            'import_path': 'chatterbot.logic.BestMatch',
            # response if chatbot doesnt understand 
            'default_response': 'I am sorry, I didnt quite catch that.',
            'maximum_similarity_threshold': 0.90
        }
    ]
    )

trainer = ListTrainer(chatbot)

# train chatbot with a choice of phrases that may be suited for some inputs from user 

# a list of things the chatbot can help with 
trainer.train([
    "What can you help me with",
    "I can help give tips on sleep, exercise.",
    "what tips can you give me",
    "I can help give tips on sleep, exercise.",
    "can you help me with my mental health",
    "I can help give tips on sleep, exercise."
])

# guidance on exercise
trainer.train([
    "Can you give me tips on exercise",
    "One of the best things to help take care of your menatl health is to do regular exercise even if its just 30 minutes of walking a day. Do you do regular exercise or do you not exercise as much as you should??",
    "I do regular exercise",
    "Well done I am proud of you <3 Remember exercise helps boost your mood and improve your physical health.",
    "I dont do much exercise",
    "Remember exercise helps boost your mood and improve your physical health.The best exercises to help your mental health and well-being is walking, hiking or even riding a bike especially in areas with nice calming scenery"
])

# guidance on sleep
trainer.train([
    "can you give me tips on sleep",
    "Make sure you dont look at screens before you sleep, or turn the blue light on to help rest your eyes. Maybe even try reading a book to help sleep. Remember you should be getting atleast 8 hours of sleep. And try to wake up around 8 so you can start your day nice and early."
])

# guidance on socialising 
trainer.train([
    "can you give me tips on socialising",
    "Keep someone close to you that you can trust and know that they will listen to you, don’t be afraid to talk about any issues you are having. I know it can be hard sometimes but try and keep social contact as good relationships are important for your mental wellbeing."
])

# guidance on school work
trainer.train([
    "can you give me tips on school work",
    "Break your work into manageable chunks and come up with a schedule to help with deadlines and plan out your assignments."
])

# links if person is struggling or needs help
trainer.train([
    "i am struggling",
    "I am sorry to hear that :( Here is a link that you may find useful to get the help you need: https://www.mind.org.uk/",
    "i need help",
    "I am sorry to hear that :( Here is a link that you may find useful to get the help you need: https://www.mind.org.uk/"
])

# response to thank you
trainer.train([
    "Thank you",
    "You're welcome :)",
])

# for url 
def index(request):
    return render(request, 'Hudson/index.html')

# response of chatbot
def getResponse(request):
    message = request.GET.get('message')
    chatbotResponse = str(chatbot.get_response(message))
    return HttpResponse(chatbotResponse)