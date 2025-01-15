# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

def get_user_list(config, key):
    try:
        # Correct path using __file__
        file_path = os.path.join(os.path.dirname(__file__), config)
        with open(file_path, "r") as json_file:
            return json.load(json_file)[key]
    except FileNotFoundError:
        print(f"Error: {config} not found in MukeshRobot directory!")
        return []
    except KeyError:
        print(f"Key '{key}' not found in {config}!")
        return []

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    ALLOW_CHATS = True  # Yeh line add karna hoga
    DATABASE_URL = "mongodb+srv://yash:shivanshudeo@yk.6bvcjqp.mongodb.net/?retryWrites=true&w=majority&appName=yk"  # MongoDB URI here
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "22180072" # integer value, dont use ""
    API_HASH = "425c7b0d42d9aa0f0b69c07687787175"
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "1786683163" # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "TMZEROO"
    SUPPORT_CHAT = "NYCreation_Chatzone"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1002321189618
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1002321189618
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://yash:shivanshudeo@yk.6bvcjqp.mongodb.net/?retryWrites=true&w=majority&appName=yk"
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = None  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "ibGjchtz3djmcaIDiG3qoLX8KE0Npo1ChFiH7QGpjoQY1uB7BGOPJ~DOT07c0VSH"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@v2ddos"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "7858950584")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "7858950584")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "7858950584")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "7858950584")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = "https://t.me/creativeydv/3" # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "7AT86JXWTFKSFSCQ"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "5LB4TAKPEKZ0"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
