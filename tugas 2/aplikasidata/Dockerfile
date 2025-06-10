# Gunakan Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy file ke image
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]
