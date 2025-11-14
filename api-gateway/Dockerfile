# Use an official Node runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application's code into the container
COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run index.js when the container launches
CMD ["node", "index.js"]
