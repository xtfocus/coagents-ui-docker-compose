FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy requirements
COPY requirements.txt .

# Install dependencies with uv (system-wide)
RUN uv pip install --system -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "-m", "research_canvas.demo"]