
FROM node:18-alpine
ENV NODE_ENV=production

WORKDIR /app/front

COPY front /app

RUN npm install --production
# && npm run build && ls -li
# FROM python:3.10-slim
# COPY --from=0 /bin/hello /bin/hello
# CMD ["/bin/hello"]
