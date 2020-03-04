#!/bin/bash

docker build -f Dockerfile -t axmouth/my_personal_site_django_server .
docker build -f postgres/Dockerfile -t axmouth/my_personal_site_postgres .
docker-compose up -d