FROM node:16.14-alpine AS build

WORKDIR /app
COPY . .
RUN yarn
RUN yarn build


FROM node:18-alpine as deploy-node
COPY --from=build /app/package.json .
COPY --from=build /app/build .
RUN HOST=0.0.0.0 PORT=3000 yarn --prod
EXPOSE 3000
CMD ["node", "index.js"]