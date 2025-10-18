from VILLAIN_MUSIC.core.bot import VILLAIN
from VILLAIN_MUSIC.core.dir import dirr
from VILLAIN_MUSIC.core.git import git
from VILLAIN_MUSIC.core.userbot import Userbot
from VILLAIN_MUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = VILLAIN()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
