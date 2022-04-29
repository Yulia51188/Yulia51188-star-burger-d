FROM node:lts

ARG APP_DIR=frontend
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

COPY package*.json ./
RUN npm ci --dev

COPY . .
EXPOSE 3000

CMD ["./node_modules/.bin/parcel", "build", "./bundles-src/index.js", "--dist-dir", "./bundles", "--public-url", "./"]


