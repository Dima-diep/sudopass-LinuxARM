File.write("/home/rootpass/pass.py", File.open("/home/rootpass/pass.py",&:read).gsub("oldpass", "newpass"))
