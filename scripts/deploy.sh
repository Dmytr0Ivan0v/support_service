#!/bin/bash

cd ~/support_service/

git pull origin master
docker-compose down && docker-compose up --build -d