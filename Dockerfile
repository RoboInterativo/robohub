
FROM node:18-alpine
# ENV NODE_ENV=production

WORKDIR /app/front

COPY front /app

RUN npm install && npm run build
# --production
# && npm run build && ls -li
FROM python:3.10-slim

COPY --from=0 /app/build /app/build
COPY back /app/back
RUN python -m venv /opt/venv &&\
    chown 1001:1001 /opt/ -R
USER 1001

RUN . /opt/venv/bin/activate &&\
        pip install pip --upgrade --cache-dir /tmp
# CMD ["/bin/hello"]
