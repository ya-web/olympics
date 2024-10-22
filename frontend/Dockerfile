# Build the React app
FROM node:18-alpine AS build

WORKDIR /frontend
COPY package*.json ./
RUN npm install --silent && npm cache clean --force
COPY . .
RUN npm run build

# Serve static files with Nginx
FROM nginx:alpine

# Define user and group environment variables
ARG USER_UID=1000
ARG USER_GID=1000
ARG USERNAME=react-user

# Switch to a non-root user:
# Install shadow tools to use useradd and groupadd
RUN apk add --no-cache shadow

RUN groupadd -g ${USER_GID} ${USERNAME} && \
    useradd -u ${USER_UID} -g ${USER_GID} -ms /bin/bash ${USERNAME}
RUN chown -R ${USERNAME}:${USERNAME} /run /var/cache/nginx /var/run /var/log/nginx && \
    chmod -R 755 /run /var/cache/nginx /var/run /var/log/nginx
USER ${USERNAME}

COPY --from=build /frontend/build /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080

# Persist Nginx logs as volume
VOLUME /var/log/nginx

CMD ["nginx", "-g", "daemon off;"]
