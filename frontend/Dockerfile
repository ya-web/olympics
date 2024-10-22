# Build the React app
FROM node:18-alpine AS build

WORKDIR /frontend
COPY package*.json ./
RUN npm install --silent && npm cache clean --force
COPY . .
RUN npm run build

# Serve static files with Nginx
FROM nginx:alpine

COPY --from=build /frontend/build /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080

# Persist Nginx logs as volume
VOLUME /var/log/nginx

CMD ["nginx", "-g", "daemon off;"]
