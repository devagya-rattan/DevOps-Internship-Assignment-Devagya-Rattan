# 1. Use an official Python runtime as a parent image
# Using a "slim" version helps keep the image size small
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only requirements first (to leverage Docker's cache)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# 1. Install necessary system tools
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 2. Run the installation script 
RUN curl -fsSL https://install.iii.dev/iii/main/install.sh | sh

# 3. Add the iii binary directories to Docker's system PATH
ENV PATH="/root/.iii/bin:/root/.local/bin:${PATH}"

# 4. Verify the installation (This will now pass successfully)
RUN iii --version


RUN iii --version
# 5. Copy the rest of your application code
COPY . .

# 6. Command to run the script
CMD ["III_URL=ws://43.205.212.249:49134 python", "math_worker.py"]
