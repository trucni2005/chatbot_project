import os

from flask import Flask, render_template, request, send_file
from chatbot_model import ChatBotModel

app = Flask(__name__)
chatbot_model = ChatBotModel()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    response = chatbot_model.get_response(user_input)
    return response

@app.route("/download_doc")
def download_doc():
    user_input = request.args.get('msg')
    key = chatbot_model.extract_key_from_input(user_input)

    if key:
        doc_path = f'BIEUMAU-TT08/{key}.doc'
        if os.path.exists(doc_path):
            return send_file(doc_path, as_attachment=True)

    return "Không tìm thấy tệp .doc phù hợp."

if __name__ == "__main__":
    app.run()
