#!/bin/bash

docker build --mount type=bind,source=/var/lib/my_personal_site/static,target=/code/mybiosite/static -f Dockerfile -t axmouth/my_personal_site_django_server .
docker build -f postgres/Dockerfile -t axmouth/my_personal_site_postgres .
docker-compose up -d