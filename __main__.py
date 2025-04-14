import os
from configparser import ConfigParser
import pulumi

aws_access_key_id=ASIAYLGLG43F3PFLHRCC
aws_secret_access_key=dyWuULnDSnKu4Jrd7/BUTbDtB/EnqOO2c0bN58mQ

credentials_path = "/home/ubuntu/.aws/credentials"
aws_dir = os.path.dirname(credentials_path)
os.makedirs(aws_dir, exist_ok=True)

config = ConfigParser()
config["default"] = {
    "aws_access_key_id": ASIAYLGLG43F3PFLHRCC,
    "aws_secret_access_key": dyWuULnDSnKu4Jrd7/BUTbDtB/EnqOO2c0bN58mQ
}

with open(credentials_path, "w") as configfile:
    config.write(configfile)

pulumi.export("archivo_credenciales", credentials_path)
