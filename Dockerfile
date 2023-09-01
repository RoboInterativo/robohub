
FROM node:18.17
COPY front /opt/front
RUN cd /opt/front &&npm install
# && npm run build && ls -li
# FROM python:3.10-slim
# COPY --from=0 /bin/hello /bin/hello
# CMD ["/bin/hello"]
