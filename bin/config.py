import configparser

config=configparser.ConfigParser()
config["id1fs"]={"path":""}
with open("./config.ini","w") as f:
    config.write(f)