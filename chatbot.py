import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a bot created for ShopEasy.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it",]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I assist you today?",]
    ],
    [
        r"quit|bye|exit",
        ["Bye! Take care. Have a great day ahead!",]
    ],
    [
        r"(.*)",
        ["Sorry, I can't understand that. Could you please rephrase?",]
    ]
]

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def shop_easy_chatbot():
    print("Welcome to ShopEasy! How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat._substitute('ShopEasy: ')
    chat._default_response = "Sorry, I can't understand that. Could you please rephrase?"

    while True:
        user_input = input("User: ")
        response = chat.respond(' '.join(tokenize(user_input)))
        print("ShopEasy:", response)
        
        if any(word in user_input.lower() for word in ["bye", "exit"]):
            print("Exiting the program...")
            break

# Run the chatbot
shop_easy_chatbot()