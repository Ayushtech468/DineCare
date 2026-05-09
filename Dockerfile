FROM python:3.12

WORKDIR /app

# Copy only requirements first (from backend)
COPY backend/requirements.txt /app/backend/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Copy backend code
COPY backend/ /app/backend/

# Set working directory inside backend
WORKDIR /app/backend

# Make entrypoint executable
RUN chmod +x scripts/entrypoint.sh

EXPOSE 8000

# Run entrypoint
ENTRYPOINT ["sh", "scripts/entrypoint.sh"]