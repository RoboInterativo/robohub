
FROM node:18-alpine
# ENV NODE_ENV=production

WORKDIR /app/front

COPY front /app

RUN npm install && npm run build
# --production
# && npm run build && ls -li
FROM python:3.10-slim
RUN mkdir /app
# ENV PYTHONHOME=/app/venv
# ENV PYTHONPATH=/app/venv/bin
COPY --from=0 /app/build /app/build
COPY back /app/back
RUN python -m venv /app/venv &&\
    chown 1001:1001 /app/ -R
USER 1001
WORKDIR /app/
RUN . /app/venv/bin/activate &&\
        pip --cache-dir /tmp install encodings &&\
        pip --cache-dir /tmp install pip --upgrade
# CMD ["/bin/hello"]
