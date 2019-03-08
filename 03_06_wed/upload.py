# https://github.com/LevPasha/Instagram-API-python/
from InstagramAPI import InstagramAPI

ig = InstagramAPI("martin.breuss", "bali2019")

ig.login()

ig.uploadPhoto("selfiechain.jpg")