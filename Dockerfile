FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080  # এই লাইনটি ক্রিটিক্যাল
CMD ["python3", "-m", "bot.main"]
