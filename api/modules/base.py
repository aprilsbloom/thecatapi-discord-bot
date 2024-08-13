import requests
from typing import Any, Dict, Optional

class Base:
	BASE_DOMAIN = "https://api.thecatapi.com/v1"

	def __init__(self, api_key: str, *, base_domain: Optional[str] = None) -> None:
		self.api_key = api_key

		if base_domain:
			self.base_domain = base_domain
		else:
			self.base_domain = self.BASE_DOMAIN

		self.headers = {
			'x-api-key': self.api_key,
			'Content-Type': 'application/json',
			'User-Agent': 'TheCatAPI Discord Bot (https://github.com/aprilsbloom/thecatapi-discord-bot)'
		}


	REQUEST_MAP = {
		"GET": requests.get,
		"POST": requests.post,
		"PUT": requests.put,
		"DELETE": requests.delete,
	}
	def make_request(
		self,
		endpoint: str,
		method: Optional[str] = "GET",
		*,
		params: Optional[dict] = None,
		data: Optional[dict] = None,
		json_data: Optional[dict] = None,
		files: Optional[dict] = None,
	) -> Dict[Any, Any]:
		request = self.REQUEST_MAP.get(method, requests.get) if method else requests.get
		try:
			res = request(
				f"{self.base_domain}/{endpoint}",
				headers=self.headers,
				params=params,
				data=data,
				json=json_data,
				files=files,
			)
			res.raise_for_status()

			try:
				return res.json()[0]
			except (requests.exceptions.InvalidJSONError, requests.exceptions.JSONDecodeError):
				return { "text": res.text }
		except requests.exceptions.ConnectionError:
			return { "error": "A connection error occurred. Please check your internet connection." }
		except requests.exceptions.Timeout:
			return { "error": "The request timed out." }
		except requests.exceptions.HTTPError as e:
			return { "error": f'A HTTP error occurred: {e}' }
		except requests.exceptions.RequestException as e:
			return { "error": f'An unknown error occurred: {e}' }