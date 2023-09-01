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
        doc_path = f'bieumau/{key}.docx'
        if os.path.exists(doc_path):
            return send_file(doc_path, as_attachment=True)

    return "Không tìm thấy tệp .doc phù hợp."

# @app.route('/handle_form_prompt', methods=['POST'])
# def handle_form_prompt():
#     user_response = request.form.get('user_response')
#
#     if user_response and user_response.lower() == 'có':
#         # Gọi hàm để mở trang web điền biểu mẫu (fill.py)
#         # Ví dụ: subprocess.run(['python', 'fill.py'])
#         # Hãy chắc chắn nhập các module cần thiết và thiết lập script fill.py của bạn.
#
#     return "Xin cảm ơn! Bạn sẽ được chuyển đến trang điền biểu mẫu."
#
# # Các tuyến đường khác và cuộc gọi app.run()

if __name__ == "__main__":
    app.run()
