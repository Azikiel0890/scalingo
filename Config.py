import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5801114104:AAHaoxGFFyxKuoqQu6VEUocIm-SKB_9zKX0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLoBu6oFvxxIK-xlaOcnYOIwzDxokUVBea9ECEgNxVWoJA3gtJkIntAlDGYhkBEdlI2IbsErpp_1zHGDC6S5530pfI-VQIYdPT9KFSXkdyAnxRleHhLOMcGlcfs_XozF0Rrzw9xV_wii3sKYSbgQNx3TO-uW6qhYkqNpxB53b9ARdfVTbSv9d44jiVrlEaUlUO85ynzwcrk4OhiNM2b-SZLsf0LinYlPyu_RnAdnBYMtbLa0gGsitzpBT0v736e4Yi0q4IC-TDB7zNQUlK4np0Jyhw0IOjfChgbIx0Oe-aSwOUoRxEADJKnTDsYzAe9WubKZkWO14nkyC7WO7-EA2ppqZqE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Aok_Musicrobot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5526868709")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
