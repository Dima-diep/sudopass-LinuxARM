File.write("/root/.bashrc", File.open("/root/.bashrc",&:read).gsub("alias sudo=\'python3 ~/sudopass/pass.py && sudo\'", " "))
File.write("/root/.zshrc", File.open("/root/.zshrc",&:read).gsub("alias sudo=\'python3 ~/sudopass/pass.py && sudo\'", " "))
