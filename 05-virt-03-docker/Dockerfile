FROM nginx:alpine

# Удаляем дефолтную страницу nginx
RUN rm -rf /usr/share/nginx/html/*

# Копируем нашу страницу для отображения 
COPY ./index.html /usr/share/nginx/html

ENV LANG en_US.UTF-8

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]
