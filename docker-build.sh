#!/bin/bash

docker build --no-cache -f Dockerfile -t axmouth/my_personal_site_django_server .
docker build --no-cache -f postgres/Dockerfile -t axmouth/my_personal_site_postgres .
docker-compose up -d