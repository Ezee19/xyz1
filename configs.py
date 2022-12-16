import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 15823382))
    API_HASH = os.getenv("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5918078029:AAHOlk_opieJ0cgVOMxOHdoHufraiaYkZHU")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOHwBuxROh2qr-6BcP1UCRZfkcHIluok6dd7WUjs5xffAzM-G14JDwcoMZgDRmvb6upddiRv3andGtavOznnsJgqOEtHnX-q4Xmj0xzV3tD_-DsUKQaif5ZyhsQC2vuykhhX06G4QojhbZx93Tp97W3qvxydhHJ_uYdh8zAYlbt0yzVf4crnhs5aKiAEcbG_OnbGzl-Xr7wl5F7GU13GgPZhyWKgJY2rgj6DO_oE78vGIHfe2EhQAqm4u4nTj-k_C0qRrVwo2fkLkaYZ0AHWjl2YmsYjouoEQ4AqcK5Kz7tyxhsL-kOPhxGf0lwFHOHn1Hnv3Dp65q1bgOVJG_cTpl1QF3rM=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1001631279048))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Mdisk_search_re_bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "5104293442"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "tlgbotsowner")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "-1001696028695")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", 'Just Search 👻')
    START_PHOTO = os.getenv("START_PHOTO", "https://graph.org/file/54e9d1cf382aaf767dd4f.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", 'Just Search 👻')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001696028695")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001683642795"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "False")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "Mdiskbotsupport")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 90))
    MDISK_API = os.getenv("MDISK_API", "XXgy4PoF35VECI7kZgTb")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", 'Just Search 👻')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", 'Just Search 👻')
