# Đọc dữ liệu từ file chứa các bài thơ
input_file_path = './data/shakespeare_char/input.txt'  # Đường dẫn đến file chứa dữ liệu thơ

with open(input_file_path, 'r', encoding='utf-8') as f:
    poetry_text = f.read()

# Loại bỏ tất cả các lần xuất hiện của "Thơ lục bát:" trong văn bản
cleaned_text = poetry_text.replace("thơ lục bát:", "")

# Lưu kết quả vào file mới
output_file_path = './data/shakespeare_char/input_cleaned.txt'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(cleaned_text)

print("Đã lưu dữ liệu sau khi loại bỏ 'thơ lục bát:' vào file:", output_file_path)
