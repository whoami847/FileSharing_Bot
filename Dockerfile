FROM python:3.9-slim

WORKDIR /app

# FFmpeg সহ প্রয়োজনীয় সিস্টেম প্যাকেজ ইনস্টল করুন
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# প্রথমে শুধু requirements.txt কপি করুন (বিল্ড অপ্টিমাইজেশনের জন্য)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# তারপর বাকি সব ফাইল কপি করুন
COPY . .

# পোর্ট এক্সপোজ করুন
EXPOSE 8080

# ENTRYPOINT হিসেবে কমান্ড সেট করুন (সবচেয়ে ভালো প্র্যাকটিস)
ENTRYPOINT ["python3", "-m", "bot.main"]
