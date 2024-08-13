from api.models import Image
from api.modules.base import Base

from dacite import from_dict
from typing import Optional

class Images(Base):
	def get_images(
		self,
		*,
		limit: Optional[int] = 1,
		breed: Optional[str] = None
	):
		res = self.make_request(
			'images/search',
			params={
				'limit': limit,
				'breed_id': breed
			}
		)

		return from_dict(Image, res)

	def get_image(self, id: int):
		pass