import os
import win32com.client as win32

# Đường dẫn đến thư mục chứa các tệp .doc
input_folder = 'bieumau'

# Đường dẫn đến thư mục đích để lưu các tệp .docx
output_folder = 'bieumau'

# Lặp qua tất cả các tệp trong thư mục đầu vào
for filename in os.listdir(input_folder):
    if filename.endswith('.doc'):
        input_filepath = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + '.docx'
        output_filepath = os.path.join(output_folder, output_filename)

        # Sử dụng win32 để chuyển đổi tệp .doc sang .docx
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(input_filepath)
        doc.SaveAs(output_filepath, FileFormat=16)  # 16 là mã định dạng cho .docx
        doc.Close()
        word.Quit()

print("Đã chuyển đổi tất cả các tệp .doc thành .docx")
