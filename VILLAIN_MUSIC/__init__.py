from VillanMusic.core.bot import Villan
from VillanMusic.core.dir import dirr
from VillanMusic.core.git import git
from VillanMusic.core.userbot import Userbot
from VillanMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Villan()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()