FROM ubuntu:18.04
# install nginx
RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update -y
RUN apt-get install -y nginx

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install --no-cache-dir grequests

ARG PUID=1000
ARG PGID=1000
ARG NGINX_HOST_HTTP_PORT=80
ARG NGINX_HOST_HTTPS_PORT=443

ENV PUID ${PUID}
ENV PGID ${PGID}
ENV NGINX_HOST_HTTP_PORT ${NGINX_HOST_HTTP_PORT}
ENV NGINX_HOST_HTTPS_PORT ${NGINX_HOST_HTTPS_PORT}

RUN adduser -D -H -u ${PUID} -s /bin/bash www-data
RUN chown -R www-data:www-data /var/lib/nginx
# expose ports
EXPOSE ${NGINX_HOST_HTTP_PORT}
# add nginx conf
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./sites/*.conf /etc/nginx/sites-available/
COPY ./services_check.py /usr/local/src
