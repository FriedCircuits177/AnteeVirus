import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D, LSTM, Input
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox

# Load NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Define text preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.lower() not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

# Define intent identification model
intent_model = Sequential()
intent_model.add(Embedding(input_dim=10000, output_dim=128, input_length=50))
intent_model.add(GlobalAveragePooling1D())
intent_model.add(Dense(64, activation='relu'))
intent_model.add(Dense(8, activation='softmax'))
intent_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Define response generation model
encoder_inputs = Input(shape=(50,))
encoder_lstm = LSTM(128)(encoder_inputs)
encoder_states = [encoder_lstm]

decoder_inputs = Input(shape=(50,))
decoder_lstm = LSTM(128)(decoder_inputs, initial_state=encoder_states)
decoder_dense = Dense(128, activation='softmax')(decoder_lstm)

response_model = Model([encoder_inputs, decoder_inputs], decoder_dense)
response_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load conversation dataset
conversations = pd.read_csv('conversations.csv')

# Preprocess conversation data
conversations['input'] = conversations['input'].apply(preprocess_text)
conversations['response'] = conversations['response'].apply(preprocess_text)

# Split data into training and testing sets
train_conversations, test_conversations = train_test_split(conversations, test_size=0.2, random_state=42)

# Train intent identification model
intent_model.fit(train_conversations['input'], train_conversations['intent'], epochs=10, batch_size=32, validation_data=(test_conversations['input'], test_conversations['intent']))

# Train response generation model
response_model.fit([train_conversations['input'], train_conversations['input']], train_conversations['response'], epochs=10, batch_size=32, validation_data=([test_conversations['input'], test_conversations['input']], test_conversations['response']))

# Define chatbot GUI
class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot")
        self.master.geometry("400x300")

        self.input_label = tk.Label(master, text="Enter your message:")
        self.input_label.pack()

        self.input_entry = tk.Entry(master, width=40)
        self.input_entry.pack()

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

        self.response_label = tk.Label(master, text="Response:")
        self.response_label.pack()

        self.response_text = tk.Text(master, width=40, height=10)
        self.response_text.pack()

    def send_message(self):
        user_input = self.input_entry.get()
        preprocessed_input = preprocess_text(user_input)
        intent = intent_model.predict(np.array([preprocessed_input]))
        response = response_model.predict([np.array([preprocessed_input]), np.array([preprocessed_input])])
        response_text = response[0]
        self.response_text.insert(tk.END, response_text + "\n")

root = tk.Tk()
chatbot_gui = ChatbotGUI(root)
root.mainloop()