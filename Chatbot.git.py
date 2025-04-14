import nltk
import random
from nltk.chat.util import Chat, reflections

# Define input and response pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a basic chatbot.", "You can call me Chatty!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "All good! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "It's okay", "No worries!"]
    ],
    [
        r"(.*) (good|great|fine)",
        ["Nice to hear that!", "That's great!"]
    ],
    [
        r"quit",
        ["Bye! Have a nice day!", "See you soon!"]
    ]
]

# Chat function
def basic_chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the chatbot
basic_chatbot()