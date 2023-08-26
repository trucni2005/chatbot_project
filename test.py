import win32com.client

def read_doc(file_path):
    word = win32com.client.Dispatch("Word.Application")
    doc = word.Documents.Open(file_path)
    content = doc.Content.Text
    doc.Close()
    word.Quit()
    return content

def save_to_txt(text, output_path):
    with open(output_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

file_path = "C:\\Users\\dangt\\chatbot_project\\bieumau\\1.doc"
output_txt_path = "C:\\Users\\dangt\\chatbot_project\\bieumau\\1.txt"

doc_content = read_doc(file_path)
save_to_txt(doc_content, output_txt_path)
print("Converted and saved to", output_txt_path)
