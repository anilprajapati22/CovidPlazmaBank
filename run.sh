#!/bin/bash
sudo su
apt update
apt install -y python3 python3-pip git sqlite3 apache2
systemctl restart apache2.service
echo 'sgn'> /var/www/html/index.html
echo 'sgnonsjkhjamjbmjkhjcsjjbjamjmjsmjlmjsmjsmjgbjkbjjbjgbjdjddjmjpjg' >  /var/www/html/sgn.html
echo 'sgn yum install'> /var/www/html/index.html
git clone https://github.com/anilprajapati22/CovidPlazmaBank.git
echo 'sgn git clone'> /var/www/html/index.html
cd CovidPlazmaBank
pip3 install -r requirements.txt
echo 'sgn python pip install'> /var/www/html/index.html
cp sgnapp.service /etc/systemd/system/
systemctl restart sgnapp.service
echo 'sgnons all done'> /var/www/html/index.html

