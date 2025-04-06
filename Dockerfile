# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /sales_analytics_ETL_dashboard

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project into container
COPY . .

# Expose Dash app port
EXPOSE 8050

# Default command (can be changed via docker-compose)
CMD ["python", "dashboard/app.py"]
