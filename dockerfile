# SỬA 1: Thêm đuôi '-bookworm' để dùng Debian 12 (Ổn định, có sẵn Java 17)
FROM python:3.9-slim-bookworm

# Cài đặt Java 17 và các thư viện cần thiết
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless procps && \
    apt-get clean

# Thiết lập biến môi trường Java
# (Đường dẫn này chuẩn cho Debian Bookworm)
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PYSPARK_PYTHON=python3

# Tạo thư mục làm việc
WORKDIR /app

# Copy file requirements và cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code vào container
COPY . .

# Lệnh mặc định
CMD ["python", "09_api_server.py"]