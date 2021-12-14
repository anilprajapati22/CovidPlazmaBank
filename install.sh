#!/bin/bash
sudo su
sudo apt update
sudo apt install python3 python3-pip git sqlite sqlite3 unzip curl -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
git clone https://github.com/anilprajapati22/CovidPlazmaBank.git
cd CovidPlazmaBank
pip3 install -r requirements.txt
python3 manage.py runserver 0:80
