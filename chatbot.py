# Importing neccessary liberies
import nltk
import random
import os 
import ssl
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression 

ssl._create_default_https_context = ssl._create_unverified_context  
nltk.data.path.append(os.path.join(os.path.abspath(), "nltk_data"))
nltk.download('punkt')

intents = [
    {  
        'tag': 'greeting',
        'patterns': ['Hi', 'Hello', 'hiii', 'Hola', 'how are you', 'hey'],
        'responses': ['Hello', 'Hey', 'Hi', 'Hola', 'Im fine, thank you!']
    },
    {
        'tag': 'goodbye',
        'patterns': ['Bye', 'Goodbye', 'See you later', 'Goodbye for now'],
    
    },
    {
        'tag': 'thanks',
        'patterns': ['Thanks', 'Thank you', "That's helpful", 'Thank you very much'],
        'responses': ['You are welcome', 'Welcome', 'You are welcome!']
    },
    {
       'tag': 'business',
         'patterns': ['What is your business', 'What do you do', 'What is your company', 'What do you offer'],
            'responses': ['We are a company that offers chatbot services', 'We are a chatbot company', 'We offer chatbot services']
    }
]