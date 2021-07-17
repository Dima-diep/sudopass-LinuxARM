with open("/home/rootpass/pass.py", "r") as f:
    raw = f.read().lower().replace("oldpass", "newpass")
    file = open("/home/rootpass/pass.py", "w")
    file.write(raw)
    file.close()
    f.close()
