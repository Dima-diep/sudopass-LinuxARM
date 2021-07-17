with open("/", "r") as f:
    raw = f.read().lower().replace("alias sudo='python3 pass.py && sudo'", " ")
    file = open("source.txt", "w")
    file.write(raw)
    file.close()
    f.close()
