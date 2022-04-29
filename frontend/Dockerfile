FROM node:lts

ARG APP_DIR=frontend
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

COPY package*.json ./
RUN npm ci --dev

COPY . ./app
EXPOSE 3000

CMD ["./node_modules/.bin/parcel", "build", "./app/bundles-src/index.js", "--dist-dir", "./app/bundles", "--public-url", "./"]


