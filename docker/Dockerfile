FROM node:18-alpine

WORKDIR /app

# Install simple HTTP server
RUN npm install -g http-server

# Copy the static files
COPY . .

# Expose port 8080
EXPOSE 8080

# Start server
CMD ["http-server", ".", "-p", "8080", "--cache", "3600", "--gzip"]
