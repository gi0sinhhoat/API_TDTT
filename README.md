# API Trả lời câu hỏi

## Thông tin sinh viên
- **Họ và tên**: Đỗ Ngọc Gia Bảo 
- **MSSV**: 24120263
- **Lớp**: 24CTT5
- **Môn học**: Tư Duy Tính Toán  

## Tên mô hình và liên kết Hugging Face
- **Tên mô hình**: `google/flan-t5-xl` 
- **link model**: [https://huggingface.co/google/flan-t5-xl](https://huggingface.co/google/flan-t5-xl)

## Mô tả 
- Hệ thống trả lời câu hỏi 
- Người dùng gửi câu hỏi qua endpoint `/answer`.
- Hệ thống sử dụng mô hình Flan-T5-XL (3B tham số).
- Có endpoint kiểm tra sức khỏe (`/health`) và trang chủ (`/`).

### Yêu cầu hệ thống
- Python 3.10 hoặc cao hơn
- RAM tối thiểu 16GB (khuyến nghị 32GB)
- GPU NVIDIA (tùy chọn, sẽ chạy nhanh hơn khi có)

### Cài đặt các thư viện cần thiết
- py -m pip install requirements.txt


### Hướng dẫn chạy chương trình
- chạy bằng cách mở file main.py
```
py main.py
```

## Hướng dẫn gọi API
### Gọi API bằng requests (Python)
```python
import requests

url = "http://127.0.0.1:9000/answer"
data = {"text": "who are you?"}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response:", response.json())
```

### Gọi API bằng curl
```bash
curl -X POST http://127.0.0.1:9000/answer \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"who are you?\"}"
```

[![Video](thumbnail.png)](video.mp4)