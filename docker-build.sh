#!/bin/bash

docker build --remove-orphans -f Dockerfile -t axmouth/my_personal_site_django_server .
docker-compose up -d