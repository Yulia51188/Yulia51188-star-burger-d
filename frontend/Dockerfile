FROM node:lts

ARG APP_DIR=frontend
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}
VOLUME ./bundles

COPY package*.json ./
RUN npm ci --dev

COPY . .
EXPOSE 3000

CMD ["./node_modules/.bin/parcel", "watch", "bundles-src/index.js", "--dist-dir", "./bundles", "--public-url", "./"]

# Run with
# docker run -d --name burger-container -v /home/yulia/docker/bundles:/frontend/bundles burger_front

