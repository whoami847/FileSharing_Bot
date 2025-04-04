FROM python:3.9-slim

WORKDIR /app

# সিস্টেম ডিপেন্ডেন্সি ইনস্টল করুন (FFmpeg লাগতে পারে)
RUN apt-get update && apt-get install -y ffmpeg

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python3", "-m", "bot.main"]  # একই কমান্ড
