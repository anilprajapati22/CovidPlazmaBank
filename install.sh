#!/bin/bash
sudo su
sudo apt update
sudo apt install python3 python3-pip git sqlite sqlite3 unzip curl -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
git clone https://anilprajapati22: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@github.com/ganpat-university/cad-project-submission-2018batch-group_10_covid_plazma.git
cd cad-project-submission-2018batch-group_10_covid_plazma
pip3 install -r requirements.txt
python3 manage.py runserver 0:80
