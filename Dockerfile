FROM python:3.9-slim  # ✅ Python 3.9 সঠিকভাবে ইনস্টল করা ইমেজ
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "-m", "bot.main"]  # ✅ python3 ব্যবহার করুন  # ✅
