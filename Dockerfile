# Bước 1: Dùng image nền có sẵn PySpark 3.2.1 (Java 8)
FROM jupyter/pyspark-notebook:spark-3.2.1

# Bước 2: Chuyển sang quyền root để cài đặt
USER root

# Bước 3: Sao chép file requirements vào (một vị trí chung)
COPY requirements.txt /tmp/requirements.txt

# Bước 4: Chạy pip install
# (Nó sẽ cài đặt streamlit, pyspark==3.2.1, v.v.)
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Bước 5: Dọn dẹp
RUN rm /tmp/requirements.txt

# Bước 6: Chuyển về user 'jovyan' (user mặc định của image này)
USER jovyan