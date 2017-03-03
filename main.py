import os
import pyperclip
import imgurpython
from credentials import credentials
from datetime import datetime


os.system("maim -s /tmp/temp.png")
timenow = str(datetime.now())
config = {
        "album" : credentials["album_id"],
        "description" : "Screenshot taken at " + timenow,
        "name" : timenow}

client = imgurpython.ImgurClient(credentials["client_id"], credentials["client_secret"],credentials["access_token"], credentials["refresh_token"])

client.upload_from_path("/tmp/temp.png", config=config, anon=False)
os.remove("/tmp/temp.png")
album = client.get_album_images(credentials["album_id"])
for image in album:
    if image.description == config["description"]:
        print(image.link)
        pyperclip.copy(image.link)
        break
print(os.path.dirname(os.path.realpath(__file__)))
os.system("mpv " + str(os.path.dirname(os.path.realpath(__file__))) + "/job-done.mp3")
