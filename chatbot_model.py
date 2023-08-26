from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import yaml
from flask import Flask, render_template, request, send_file
import os

class ChatBotModel:
    def __init__(self):
        self.chatbot = self.create_chatbot()
        self.train_chatbot()

    def extract_key_from_input(self, user_input):
        keywords = ["hồ sơ thầu"]
        keyword_hello = ["chào", "hello", "hi"]
        keyword_bye = ["tạm biệt", "cảm ơn"]
        key = None

        user_input = user_input.lower()

        for keyword in keyword_hello:
            if keyword in user_input:
                return 1

        for keyword in keyword_bye:
            if keyword in user_input:
                return 0

        for keyword in keywords:
            if keyword in user_input:
                key = user_input.split(keyword)[-1].strip()
                print(key)
                break

        return key

    def create_chatbot(self):
        chatbot = ChatBot("VietnameseBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
        return chatbot

    def train_chatbot(self):
        yaml_file_path = 'custom_corpus.yml'

        with open(yaml_file_path, 'r', encoding='utf-8') as file:
            yaml_parser = yaml.SafeLoader
            data = yaml.load(file, Loader=yaml_parser)

        conversations = data.get('conversations', [])
        training_data = []

        for conversation in conversations:
            training_data.append([message[0] for message in conversation])

        trainer = ChatterBotCorpusTrainer(self.chatbot)
        print("Chatbot training started.")
        trainer.train('custom_corpus')
        print("Chatbot training completed.")

    def get_response(self, user_input):
        key = self.extract_key_from_input(user_input)

        if key == '':
            response = "Được thôi, bạn cần bộ hồ sơ nào vậy?"

        elif key == 1:
            response = "Chào bạn, bạn cần hỗ trợ gì ạ?"

        elif key == 0:
            response = "Cảm ơn bạn đã sử dụng chatbot của chúng tôi. Nếu có bất kì câu hỏi nào khác, vui lòng liên hệ lại cho chúng tôi. Chúng tôi rất sẵn lòng hỗ trợ bạn"

        elif key:
            doc_path = f'bieumau/{key}.doc'
            if os.path.exists(doc_path):
                return f"Tải về tệp .doc: <a href='/download_doc?msg={user_input}'>{key}.doc</a>"

        else:
            response = str(self.chatbot.get_response(user_input))

        return response
