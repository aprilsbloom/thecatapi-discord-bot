from dataclasses import dataclass

@dataclass
class Image:
	id: int
	url: str
	width: int
	height: int