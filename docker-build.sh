#!/bin/bash

docker build -f Dockerfile -t axmouth/my_personal_site_django_server .
docker-compose up -d --remove-orphans