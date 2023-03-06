#!/bin/bash

cd ~/support_service/

git pull
docker-compose down && docker-compose up --build -d