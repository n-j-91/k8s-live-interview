FROM alpine:latest as production_image

RUN apk update \
  && apk add nginx

RUN adduser -D -g 'www' www \
  &&  mkdir /www \
  && chown -R www:www /var/lib/nginx \
  && chown -R www:www /www

COPY ./nginx.conf /etc/nginx/
COPY ./index.html /www/

ENTRYPOINT ["nginx", "-g", "daemon off;"]