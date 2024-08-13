from api.modules import Images, Breeds, Favourites, Votes

class TheCatAPI():
	def __init__(self, key: str) -> None:
		self.images = Images(key)
		self.breeds = Breeds(key)
		self.favourites = Favourites(key)
		self.votes = Votes(key)