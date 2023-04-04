#!/bin/bash

cd support_service

git pull
sudo docker-compose down && sudo docker-compose up --build -d